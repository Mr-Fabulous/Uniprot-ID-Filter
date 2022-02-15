# -*- coding: utf-8 -*-
# @Author: leomiao
# @Date:   2021-11-17 15:36:06
# @Last Modified by:   leomiao
# @Last Modified time: 2021-11-21 16:58:53
# match uniprot id in no_pdb with files (downloaded from Alphafold) 
import os
from shutil import copyfile
no_pdb = {}
filename = 'no_pdb.txt'
with open(filename) as file:
    for line in file:
        l = line.rstrip()
        #print(l)
        no_pdb[l] = True
#print(no_pdb)


# Folder path from Alphafold
folder_path = './Alphafold'
folder_path_list = []
import shutil, errno
if not os.path.isdir(folder_path):
    print('Folder path not exist!')

#-----------------------------------------
# open previous text file

file1 = "no_predicted_list_part1.txt"
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
		no_pre += 1
print(pre)
print(no_pre)

#-----------------------------------------
counter = 0
for root, dirs, files in os.walk(folder_path, topdown=True):
    for name in files:
        if not name[-6:]=='pdb.gz':
            continue
        uniprotid  = name.split('-')[1]   # ex: AF-uniprotid-XXX
        if uniprotid in no_pdb:
        	no_pdb[uniprotid] = True
        	counter += 1
print('Out of ', len(no_pdb), 'uniprot ids' )
print(counter, ' with predicted struture.')


f= open("predicted_list.txt","w+")

for key in no_pdb:
    if no_pdb[key] == True:
        f.write("%s\n" % key)

f= open("no_predicted_list.txt","w+")

for key in no_pdb:
    if no_pdb[key] == False:
        f.write("%s\n" % key) 