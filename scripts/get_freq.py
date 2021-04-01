import numpy as np
import csv
import sys, os
import pandas as pd
from collections import defaultdict

#taking input
in_file = input("Input filepath: ") # the file from which frequencies are to be collected

outfile = input("Output filepath: ") # the file to which all the stuff will be written

ann_file = input("Annotation file: ") # the file in which gene data and lengths are stored

# creating a list of gene IDs from ann_file; and a dict with all data from ann_file
with open (ann_file, "r", newline= "") as ann:
    ann_reader = csv.DictReader(ann, delimiter = "\t") ## change the "\t" to "," if your annotation file is comma-separated
    gene_list = []
    length_list = []
    ann_dict = defaultdict(list)
    for row in ann_reader:
        genes = row["GeneID"]
        gene_list.append(genes)
        l = row["Length"]
        length_list.append(l)
        for gene, data in row.items():
            ann_dict[gene].append(data)
#print(gene_list)
#print(ann_dict)
alt_ann_dict = dict(zip(gene_list, length_list))
#print(alt_ann_dict)
#print("next dict")
ann.close()

# calculating frequecies of each gene
with open (in_file, "r", newline = "") as snv_file:
    in_filereader = csv.DictReader(snv_file, delimiter = "\t")
    snv_list = []
    for row in in_filereader:
        gene_name = row["GeneID"]
        snv_list.append(gene_name)
gene, counts = np.unique(snv_list, return_counts= True)
snv_freq = np.asarray((snv_list, counts), dtype = "object").T
#print(snv_freq_list)
#print(snv_freq)
print(type(gene))
print(type(counts))

freq_keys = gene.tolist()
freq_vals = counts.tolist()
freq_dict = dict(zip(freq_keys, freq_vals))
#print(freq_dict)

# matching gene to gene frequency
len_freq_dict = {}
for key_freq, freq in freq_dict.items():
    for key_len, len_value in alt_ann_dict.items():
        if key_freq in key_len:
            if len_value == "-":
                pass
            else:
                len_freq_dict[key_freq] = [freq, len_value, round((float(freq)/float(len_value)), 5)]
            #print("Working on", key_freq, "...")
        else:
            pass

#print(len_freq_dict)

with open (outfile, "w", newline= "") as out:
    out_writer = csv.DictWriter(out, delimiter = "\t", fieldnames= ["GeneID", "SNV_Frequency", "Gene_Length", "Relative_Freq([1]/[2])"])
    out_writer.writeheader()
    for k, v in len_freq_dict.items():
        out_writer.writerow({"GeneID": k, "SNV_Frequency": v[0], "Gene_Length": v[1], "Relative_Freq([1]/[2])": v[2]})
out.close()

## done, hopefully
