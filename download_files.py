# -*- coding: utf-8 -*-
# @Author: leomiao
# @Date:   2021-11-17 17:20:39
# @Last Modified by:   leomiao
# @Last Modified time: 2022-02-27 15:54:41

# Download pdb files from AlphaFold: http://ftp.ebi.ac.uk/pub/databases/alphafold/latest/
import os
import wget
import argparse

parser = argparse.ArgumentParser(description='Download')
parser.add_argument('--file_index', default=0, type=int, help='file index')    #Specify which file to download in the list
opt = parser.parse_args()
file_ind = opt.file_index

def download_files(url_file, destination_path):
    # Create a new directory if it does not exist 
    if not os.path.exists(destination_path):
      os.makedirs(destination_path)

    url_list = []
    with open(url_file) as file:
        for line in file:
            data = line.rstrip()
            print(data)
            url_list.append(data)
    

    '''for download_url in url_list:
        filename = download_url.split('/')[-1]
        print('Downloading from: ' + download_url)
        wget.download(download_url, destination_path + '/' + filename)'''
    download_url = url_list[file_ind]
    print(file_ind)
    filename = download_url.split('/')[-1]
    print('Downloading from: ' + download_url)
    wget.download(download_url, destination_path + '/' + filename)
    

# Call download_files function
url_file = 'url_list.txt'                                       #list to download from AlphaFold website
destination_path = './pdb_files'                                #Download to this directory
download_files(url_file, destination_path)




