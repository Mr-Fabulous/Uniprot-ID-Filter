# -*- coding: utf-8 -*-
# @Author: leomiao
# @Date:   2022-03-01 14:00:30
# @Last Modified by:   leomiao
# @Last Modified time: 2022-03-01 17:42:05
# import required module
import os
import tarfile
from pathlib import Path

# assign directory
directory = './AlphaFold'
 
# iterate over files in the directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        if filename.endswith((".tar")):
            folder_path = os.path.join(directory, filename[:-4])
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            tar = tarfile.open(f)
            print("Extracting ", folder_path, "...")
            tar.extractall(path=folder_path)
            tar.close()