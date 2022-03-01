<h1 align="center"> Uniprot-ID-Filter </h1>
A script for filtering Uniprot Ids.

## Usage
Given the Uniprot Ids, this script filters out the Uniprot Ids with (predicted) pdb structures from [AlphaFold](https://alphafold.ebi.ac.uk/) with the corresponding pdb files.


Input file for this script: 
1. Your Uniprot Id list (txt file format).

Output files for this script:
1. have_pdb_list.txt: Uniprot ID list with predicted pdb structure.
2. no_pdb_list.txt: Uniprot ID list with no predicted pdb structure.

<img src="https://github.com/Mr-Fabulous/Uniprot-ID-Filter/blob/main/pipeline.png" width="600" height="320">

## Prerequisites

- Python 3.6

## Tutorial
1. Create a directory named AlphaFold; This directory is used to store all the compressed prediction files downloaded from AlphaFold DB.
```sh
    mkdir AlphaFold
``` 
2. Run the script run_download.sh; This script runs download_files.py for multiple times to download all the files from this [link](http://ftp.ebi.ac.uk/pub/databases/alphafold/latest/).
3. Run the script filter.sh; This script runs unzip.py and then runs match_uniprot_id.py. The file unzip.py unzips all the files downloaded in step 2; The file match_uniprot_id iterates through every unzipped pdb files and then filters out our target files(based on the provided list). 
4. After the above three steps are done, two output files will be generated (have_pdb_list and no_pdb_list). The targeted pdb files (which are the corresponding pdb files for the uniprot IDs with predicted strctures) are stored in the folder matched_pdb(automatically generated in step 3).

