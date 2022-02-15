# Uniprot-ID-Filter
A script for filtering Uniprot Ids.

## Usage
Filters out Uniprot Uds with (predicted) pdb structures from [AlphaFold](https://alphafold.ebi.ac.uk/).

Input file for this script: 
1. Your Uniprot Id list (txt file format).

Output files for this script:
1. predicted_list.txt: Uniprot ID list with predicted pdb structure.
2. no_predicted_list.txt: Uniprot ID list with no predicted pdb structure.


## Prerequisites

- Python 3.6

## Tutorial
1. Create a directory named AlphaFold; This directory is used to store all the compressed prediction files downloaded from AlphaFold DB.
```sh
    mkdir AlphaFold
``` 
2. Download all the compressed prediction files to the directory from [here](https://www.alphafold.ebi.ac.uk/download).
3. Unzip all the compressed files.
4. Run match_uniprot_id.py. The script will run through every pdb files under the AlphaFold directory and filter out the Uniprot IDs.
```sh
    python match_uniprot_id.py
``` 
