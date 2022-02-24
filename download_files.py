# -*- coding: utf-8 -*-
# @Author: leomiao
# @Date:   2021-11-17 17:20:39
# @Last Modified by:   leomiao
# @Last Modified time: 2022-02-24 15:26:15

# Download pdb files from AlphaFold: http://ftp.ebi.ac.uk/pub/databases/alphafold/latest/
import os
import requests
import wget
from bs4 import BeautifulSoup


def download_files(url, destination_path):
    # Create a new directory if it does not exist 
    if not os.path.exists(destination_path):
      os.makedirs(destination_path)

    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    branches = []
    for link in soup.find_all('a'):
        branch = link.get('href')
        if branch[:2] == 'UP':
            branches.append(branch)

    for branch in branches:
        filename = branch.split('/')[-1]
        download_url = url + branch
        print('Downloading from: ' + download_url)
        wget.download(download_url, destination_path + '/' + filename)


# Call download_files function
url = 'http://ftp.ebi.ac.uk/pub/databases/alphafold/latest/'    #AlphaFold download url
destination_path = './pdb_files'                                #Download directory
download_files(url, destination_path)




