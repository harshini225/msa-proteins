# msa-proteins
CSCI 2820 final project 

Several pieces of code and intermediate data files are included in this repository. 

## Code written 
Here are general desciptions on each of the programs and their purpose. There are more detailed
comments within each file when necessary. 

### dcmp_analysis.py

This program analyses the DCMP files (Database for Cancer Mutant Proteins) to find the 
most common cancer mutant protein domains across various types of cancers. 

### process_uniprot.py

This program analyses the Uniprot sequences and groups them by protein domain to prepare
for Multiple Sequence Alignment. 

### print_summary_stats.py

This program calculates the average percent similarity from the alignments and percent similarity matrix data. 

### make_graphs.py

This program makes all graphs using MatPlotLib. 

### make_files.sh

This program makes text files with the names of cancers to assist in organising data from DCMP. 

## Intermediate data files

Data from the cancers and cancer mutant protein domains are in the sig-cancers folder. 

Sequences (input to alignmers) are in the sequences folder. 

Results from online multiple sequence alignment are in the results folder, grouped by protein, alignment input. The aligner used is in the filename. 

Graphs are included in the graphs folder. 