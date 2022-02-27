#!/bin/bash
for i in {0..47}
do
   python download_files.py --file_index=$i
done

