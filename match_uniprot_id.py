# -*- coding: utf-8 -*-
# @Author: leomiao
# @Date:   2021-11-17 15:36:06
# @Last Modified by:   leomiao
# @Last Modified time: 2022-03-01 16:16:33
# match uniprot id in no_pdb with files (downloaded from Alphafold) 
# filter out the uniprot ids with no predicted pdb strucutres
import os
from shutil import copyfile
uniprot_id_list = {}
filename = 'prot_uniprotID_not_repeated.txt'     #target file with your own uniprot ids
with open(filename) as file:
    for line in file:
        l = line.rstrip()
        #no_pdb[l] = True
        uniprot_id_list[l] = False



# Folder path from Alphafold
folder_path = './AlphaFold'
folder_path_list = []
import shutil, errno
if not os.path.isdir(folder_path):
    print('Folder path not exist!')

destination_path = './matched_pdb'
if not os.path.isdir(destination_path):
    os.mkdir(destination_path)

#-----------------------------------------
# open previous text file if needed

'''file1 = "no_predicted_list_part1.txt"
with open(file1) as file:
    for line in file:
        l = line.rstrip()
        no_pdb[l] = False

no_pre = 0
pre = 0
for key in no_pdb:
	if no_pdb[key] == True:
		pre += 1
	else:
		no_pre += 1'''


#-----------------------------------------
counter = 0
for root, dirs, files in os.walk(folder_path, topdown=True):
    for name in files:
        if not name[-6:]=='pdb.gz':
            continue
        uniprotid  = name.split('-')[1]   # ex: AF-uniprotid-XXX
        if uniprotid in uniprot_id_list:
            uniprot_id_list[uniprotid] = True
            counter += 1
            curr_path = os.path.join(root, name)
            shutil.copy(curr_path, destination_path + '/' + name)
print('Out of ', len(uniprot_id_list), 'uniprot ids' )
print(counter, ' with predicted struture.')


# output two files: 1. uniprot ids with predicted structures 2. uniprot ids with no predicted structures
f= open("have_pdb_list.txt","w+")

for key in uniprot_id_list:
    if uniprot_id_list[key] == True:
        f.write("%s\n" % key)

f= open("no_pdb_list.txt","w+")

for key in uniprot_id_list:
    if uniprot_id_list[key] == False:
        f.write("%s\n" % key) 