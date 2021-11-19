## this version of get_freq collects %AT-richness, gene expression data and SumFreq statistic on top of the data collated by get_freq.py
import pandas as pd
import numpy as np

## NOTE: All filenames are placeholders
raw = pd.read_csv("REDItools_processed_dedup-filt.genann.txt", header = 0, sep = "\t")
exp = pd.read_csv("Expression_Data/quant.sf", header=0, sep="\t")

at_richness = pd.read_csv("at_richness.txt", header=0, sep="\t")
gene_ann = pd.read_csv("Gene_Length_Data.txt", header = 0, sep = "\t")

counting = raw[["GeneID", "Frequency"]]
#print(test.head(5))
counting["NumLoci"] = 1
counting = counting.groupby("GeneID", as_index = False).sum()
counting = counting[counting["GeneID"] != "-"]

merged = pd.merge(counting, gene_ann, on = "GeneID")
merged = merged[["GeneID", "Frequency", "NumLoci", "Length", "TranscriptID"]]
merged["AvgFreq"] = merged["Frequency"]/merged["NumLoci"]

exp_merged = pd.merge(merged, exp, left_on="TranscriptID", right_on="Name")

exp_mergedClean = exp_merged[["GeneID", "Frequency", "NumLoci", "Length_x", "TranscriptID", "AvgFreq", "Name", "TPM", "NumReads"]]
exp_mergedClean.rename(columns = {"Frequency" : "SumFreq"}, inplace=True)

final_merged = pd.merge(exp_mergedClean, at_richness, on="TranscriptID")
final_merged = final_merged[["GeneID", "SumFreq", "NumLoci", "Length_x", "TranscriptID", "AvgFreq", "TPM", "NumReads", "%AT_Richness"]]
final_merged["SumFreq"] = final_merged["SumFreq"].round(decimals = 3)
final_merged["AvgFreq"] = final_merged["AvgFreq"].round(decimals = 3)
final_merged["%AT_Richness"] = final_merged["%AT_Richness"].round(decimals = 3)
final_merged["TPM"] = final_merged["TPM"].round(decimals = 3)
final_merged.rename(columns = {"Length_x" : "Length"}, inplace=True)

#print(final_merged.head(5))

final_merged.to_csv("Sample_getFreq.txt", sep = "\t", header = True, index = False)
