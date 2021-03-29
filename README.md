# Contextualize-SNVs
A set of tools which can be used to put single-nucleotide variations (SNVs) in context. Includes *stack_genes.py, get_spans.py and get_freq.py*. These scripts were used to generate the analysis presented in >Pervasive_SNVs_Publcation<. Data input(s) are tab-separated tabular files.

# stack_genes.py

This script takes as input the following:
1. Number of bins to divide each gene into
2. Absolute filepath to an input file. This file must contain the columns "Position", referring to the SNV position on the **chromosome**, and "GeneID", referring to the gene on which the SNV occurs
3. Sample name (whatever base name you would like to apply to the output files)
4. A GTF file, prepared as described below
5. Absolute path to the output directory

The script first splits the data file by chromosome number into multiple "chromosome files". The data file must necessarily contain the columns "Region" (i.e. chromosome number), "Position" (i.e. the position of the SNV on the chromosome) and "GeneID" (i.e. the name/ID of the gene corresponding to each SNV). 

It then divides each gene in the input data into n equal-sized bins (n is user specified) using gene start/end data from the GTF file and assigns each SNV to a particular bin, creating a histogram of SNV occurrence over a particular gene. It iterates this histogram construction over all unique genes in the data and averages the resulting histogram arrays as a last step, creating a global view of SNV distribution. Additionally, it also creates such an averaged histogram for each chromosome separately. For user reference, the script further outputs a table containing the bin number and its (averaged) frequency (of occurrence of SNVs in that bin). Lastly, it creates a tabular stats_file.txt, which contains the following columns:
1. Chr (The filepath of the chromosome file)
2. #Unannotated Hits (the number of SNVs which were not annotated with a gene ID)
3. #Genes Processed (the number of unique genes found in that chromosome file)



