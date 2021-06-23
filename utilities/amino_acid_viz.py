## importing
import os
import pandas as pd
import csv
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

## a dictionary defining 10 groups of amino acids/placeholders
AA_Table = {"Simple":["Gly", "Ala", "Val", "Leu", "Ile"],"Aromatic":["Phe", "Tyr", "Trp"],"Basic":["Lys", "Arg"],"Acidic":["Asp", "Glu"],"Hydroxyl":["Ser", "Thr"],"Amide":["Asn", "Gln"],"S_containing":["Met", "Cys"],"Amid_Aro":["His", "Pro"],"Stop":["Ter"], "Del":["*"]}

## this function annotates amino-acid changes using the dict AA_Table and can output (in order of occurrence), 1. a heatmap of type-changes (eg. acidic to basic, etc) -- annotated as HEATMAP1 in the function; 2. a heatmap of amino acid changes (eg. Gly to Pro, etc) -- annotated below as HEATMAP2; and 3. a clustermap of amino acid changes -- annotated as CLUSTERMAP. Unhash as needed below.
def make_table(file):
    name_list = ["CHROM", "POS", "REF", "ALT", "EFFECT", "AA_EFECT", "AA_CHANGE", "FROM-TO"]
    data = pd.read_csv(file, header=0,sep="\t")
    dataf = pd.DataFrame(data)
    dataf.columns = name_list
    dataf.fillna("None", inplace=True)
    #print(dataf.head(10))
    dataf[["From", "To"]] = dataf["FROM-TO"].str.split("-", n = 1, expand = True)
    #print(dataf.head(10))
    dataf["Type_FROM"] = dataf.apply(lambda row : classify(row["From"]), axis = 1)
    dataf["Type_TO"] = dataf.apply(lambda row : classify(row["To"]), axis = 1)
    dataf["Type_From_To"] = dataf.apply(lambda row : fuse_for_count(row["Type_FROM"], row["Type_TO"]), axis = 1)
    print(dataf.head(10))
    type_list = dataf["Type_From_To"].to_list()
    type_list = [x for x in type_list if x != "None-None"]
    type_change, counts = np.unique(dataf["Type_From_To"], return_counts=True)
    #print(type_change)
    #print(counts)
    type_change_dict = {A: B for A,B in zip(type_change,counts)}
    #print(type_change_dict)
    df_type_change =pd.DataFrame.from_dict(type_change_dict, orient='index')
    df_type_change.reset_index(inplace=True)
    df_type_change.columns = ["Type", "Count"]
    df_type_change[["From", "To"]] = df_type_change["Type"].str.split("-", n = 1, expand = True)
    #print(df_type_change.head(10))

    #df_type_change.to_csv("./test_matrix.tst", sep="\t", index=False)

    df_type_change = df_type_change.pivot("From", "To", "Count")
    ## HEATMAP1
    #sns.heatmap(df_type_change, vmin=0, vmax=3500, center=1500.0, linewidths=.5, cmap = "icefire", annot=True, fmt="n", annot_kws={"fontsize":6}) ## example_AA_typeshift
    #plt.show()

    change, c_counts = np.unique(dataf["FROM-TO"], return_counts=True)
    change_dict = {A: B for A,B in zip(change,c_counts)}
    df_change = pd.DataFrame.from_dict(change_dict, orient='index')
    df_change.reset_index(inplace=True)
    df_change.dropna(axis=1)
    names = ["Change", "Count"]
    df_change.columns = names
    df_change[["From", "To"]] = df_change["Change"].str.split("-", n = 1, expand = True)
    #print(df_change.head(10))
    #df_change.to_csv("./aa_change.test_matrix.txt", sep="\t", index=False)
    df_change.fillna("None", inplace=True)
    change_heatmap = df_change.pivot("From", "To", "Count")
    change_heatmap.fillna(0)
    
    ## HEATMAP2
    #ax = sns.heatmap(change_heatmap, vmin=0,vmax=1500, linewidths=.5, cmap = "viridis_r", annot=True, fmt="n", annot_kws={"fontsize":5}, square=True, xticklabels=1)
    #ax.set_xticklabels(ax.get_xmajorticklabels(), fontsize = 10)
    #plt.show()
    
    #print(df_change.head())
    
    ## CLUSTERMAP
    cluster_data = pd.pivot_table(df_change, values="Count", index="To", columns="From", fill_value=0.00000000000001)
    #print(cluster_data.head())
    res = sns.clustermap(cluster_data, figsize=(7, 5),vmin=0,vmax=1500, cmap = "viridis_r",linewidths=.2, yticklabels=1, annot=True, fmt="n", annot_kws={"fontsize":5}, cbar_pos=None)#, metric="correlation")
    res.ax_heatmap.set_xticklabels(res.ax_heatmap.get_xmajorticklabels(), fontsize = 10)
    res.ax_heatmap.set_yticklabels(res.ax_heatmap.get_ymajorticklabels(), fontsize = 8)
    #plt.title("The Profile of Amino Acid Changes (test_sample)")
    #plt.savefig(""./aa_figure.svg", format="svg")
    #plt.savefig("./aa_figure.png", format="png")
    plt.show()

## this function classifies amino acids in the data file according to the dict AA_table
def classify(string):
    for aa, codon in AA_Table.items():
        if string in codon:
            return(aa)

## this function returns a fusion of strings as string1-string2
def fuse_for_count(s1, s2):
    return(str(s1)+"-"+str(s2))

input_file = input("Output file of snpSift.sh, containing data about amino-acid changes (absolute path): ")
make_table(input_file)

## done, hopefully
