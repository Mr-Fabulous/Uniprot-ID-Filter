# -*- coding: utf-8 -*-
# @Author: leomiao
# @Date:   2022-02-24 16:26:44
# @Last Modified by:   leomiao
# @Last Modified time: 2022-02-24 16:52:25
import os
import requests
from bs4 import BeautifulSoup

def generate_list(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    branches = []
    for link in soup.find_all('a'):
        branch = link.get('href')
        if branch[:2] == 'UP':
            branches.append(branch)

    f = open("url_list.txt","w+")   #create a txt file to store urls
    for branch in branches:
        filename = branch.split('/')[-1]
        download_url = url + branch
        f.write('%s\n'% download_url)



generate_list(url = 'http://ftp.ebi.ac.uk/pub/databases/alphafold/latest/')
        