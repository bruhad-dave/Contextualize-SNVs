# Contextualize-SNVs
A set of tools which can be used to put single-nucleotide variations (SNVs) in context. Most of the work is done by *stack_genes.py, get_spans.py and get_freq.py*. These scripts were used to perform the analysis and generate the figures presented in the work titled "Exceptionally high sequence-level variation in the transcriptome of Plasmodium falciparum" (preprint@ https://www.biorxiv.org/content/10.1101/2021.05.14.444266v1). Data input(s) are tab-separated tabular files.

# stack_genes.py

This script is wrapped in **stack_a_bunch.sh**, which takes as input the following:
1. Number of bins to divide each gene into
2. Absolute filepath to an input file. This file must contain the columns "Position", referring to the SNV position on the **chromosome**, and "GeneID", referring to the gene on which the SNV occurs
3. A GTF file, prepared as described below
4. Absolute path to the output directory

The script first splits the data file by chromosome number into multiple "chromosome files". The data file must necessarily contain the columns "Region" (i.e. chromosome number), "Position" (i.e. the position of the SNV on the chromosome) and "GeneID" (i.e. the name/ID of the gene corresponding to each SNV). 

It then divides each gene in the input data into n equal-sized bins (n is user specified) using gene start/end data from the GTF file and assigns each SNV to a particular bin, creating a histogram of SNV occurrence over a particular gene. It iterates this histogram construction over all unique genes in the data and averages the resulting histogram arrays as a last step, creating a global view of SNV distribution. Additionally, it also creates such an averaged histogram for each chromosome separately. For user reference, the script further outputs a table containing the bin number and its (averaged) frequency (of occurrence of SNVs in that bin). Lastly, it creates a tabular stats_file.txt, which contains the following columns:
1. Chr (The filepath of the chromosome file)
2. #Unannotated Hits (the number of SNVs which were not annotated with a gene ID)
3. #Genes Processed (the number of unique genes found in that chromosome file)

This script generates Figure 1B.

# get_spans.py

This script is wrapped in **spans.sh**, which takes as input the following:
1. the number of flanking nucleotides around each SNV to extract (i.e., if this option is given the value 2, the program will extract 2 nucleotides on both side of the SNV position and the output would be a pentamer)
2. a reference genome file in fasta format
3. Absolute path to input file

This script outputs a span_file.txt (containing spans in a format that can be used with samtools faidx), a span_data_file.txt (which includes verbose information about each span) and a spans.txt file, containing the span sequence extracted from the user-input reference fasta file. It also runs span_analysis.py on each span in the spans.txt file, which outputs a heatmap of all flankning sequence motifs which occur at a frequency of 150 or higher.

## spans_v2.sh
This script wraps around get_span_v2.py, samtools, get_span_strcorr.py, and span_analysis_v2.py
These are the outputs included in the most recent version of the manuscript. This script also generates heatmaps in Figures 2E and S8.

# get_freq.py

This script takes as input the following:
1. Absolute filepath for input file
2. Absolute filepath for output file (including filename)
3. Absolute file path to an annotation file containing gene start/end information (tab separated, must contain

This script outputs a file containing the following columns:
1. GeneID
2. SNV_Frequency
3. Gene_Length
4. Relative Frequency (values in column2/ values in column3)

## get_freq_v2.py
Updated from the above, outputs a larger set of data about each SNV position, including expression data (TPM, number of reads), %AT-ruchness, and the SumFreq statistic used in the manuscript. Outputs of get_freq_v2.py were used to generate Figures S5 and S6.

# Other scripts
Other scripts in this repository include:
- REDI_2_snpEff.in.sh: converts REDItools2.0 output files to a VCF-like format
- REDI_filter.sh: filters REDItools2.0 output files
- run_snpEff.sh: runs snpEff on a folder containing input files (which may be generated from REDItools2.0 output using REDI_2_snpEff.in.sh)

# Scripts in /utilities/
- get_at_richness.py: returns the AT-richness of each fasta record in a CDS file in tabular format
- snpSift.sh: returns a VCF-like file with easily readable information about amino acid changes
- amino_acid_viz.py: a script that plots three kinds of visualizations representing amino acid changes, a heatmap of type-changes (eg. Acidic to Basic etc), a heatmap of amino acid changes (eg. Gly to Pro, etc), and a clutermap of amino acid changes; Requires output from snpSift.sh as input. Used to generate Figure 2D and Figure S7.
- do_htseq.sh: wraps around htseq (https://htseq.readthedocs.io/en/master/)

# Scripts in /plotting/
- scripts used to generate the figures presented in the manuscript.

# The scripts in this repository depend on/import
- Python 3.8 
- Pandas
- Matplotlib
- Biopython
- Numpy
- Seaborn
- snpEff and snpSift
- argparse, sys, os


