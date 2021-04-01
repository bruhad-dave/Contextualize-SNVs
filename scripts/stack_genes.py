#importing
import pandas as pd
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import argparse
import csv

##parsing arguments
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--nbins", type=int, help="The number of bins to divide each gene into")
parser.add_argument("-i", "--infile", help="Input file containing SNV data")
parser.add_argument("-s", "--sample", help="The name of the sample (will be applied to any output files)")
parser.add_argument("-a", "--gtf", help="The reference file in modified gtf format")
parser.add_argument("-o", "--outdir", help="The base directory for outputs")
args = parser.parse_args()
nbins = args.nbins
sample = args.sample
infile = args.infile
gtf = args.gtf
OUT_DIR = args.outdir

if not nbins:
    nbin = 100
if not sample:
    print("No sample name given. Outputs will be prefixed with 'sample'.")
    sample = "sample"
if not gtf:
    print("No annotation file given.")
    quit()
if not infile:
    print("No input file given.")
    quit()
if not OUT_DIR:
    OUT_DIR = "./"

##
#initializing variables
chr_no = 14 ## change this based on your organism of interest
total_hists = []
bin_sizes = []
def stack_genes(file, bin_no, ann_file): ## function that does the heavy lifting
    global total_hists
    global bin_sizes
    print("Working...")
    #import data, including only Region, Position, GeneID
    data = pd.read_csv(file, sep="\t", header=0, usecols=["Position", "GeneID"])
    unique_genes, gene_freq = np.unique(data["GeneID"], return_counts=True)
    gene_freq_dict = dict(zip(unique_genes, gene_freq))
    a = data.groupby("GeneID")
    b = a["Position"].apply(lambda s: s.tolist())
    pos_dict = b.to_dict()
    #print(pos_dict)
    nc_list = list(map(int, pos_dict["-"]))
    print(len(nc_list))

    #import reference data

    gtf_data = pd.read_csv(ann_file, sep=",", header=0)
    num_genes = len(np.unique(gtf_data["GeneID"]))
    avg_length = np.average(gtf_data["Length"])
    c = gtf_data.groupby("GeneID")
    ref_dict = gtf_data.set_index("GeneID").T.to_dict("list")
    #print(ref_dict)


    counta_5 = []               ## will contain hits 1kb from start -- putative 5' UTR
    counta_3 = []               ## will contain hits 1kb from end -- putative 3' UTR
    unannoated_nc_hits = []     ## will contain hits not annotated by a gene or a UTR
    lengths = []
    histogram_dict = {}         ## will contain gene, histogram pairs
    hist_over_all_genes = []    ## is a list of histogram arrays, one for each gene
    utr_dict = {}
    stack_dict = {x:(pos_dict[x], ref_dict[x]) for x in pos_dict if x in ref_dict}

    for gene, values in stack_dict.items():
        snv_list, ref = values
        #snv_list = list(map(int, snv_list))
        #ref = list(map(int, ref))
        #print(ref)
        hist, bins = np.histogram(snv_list, bins = nbins, range = (ref[0], ref[1]))
        hist_as_list = hist.tolist()
        hist_over_all_genes.append(hist_as_list)
        lengths.append(ref[1]-ref[0])
        histogram_dict.update({gene : hist_as_list})

        for i in nc_list:
            if i in range(ref[0]-1000, ref[0]):
                counta_5.append(i)
                #nc_list.remove(i)
            elif i in range(ref[1], ref[1]+1000):
                counta_3.append(i)
                #nc_list.remove(i)
            else:
                unannoated_nc_hits.append(i)

    commonlist = []
    for m in counta_5:
        if m in counta_3:
            commonlist.append(m)
    genes_processed_list = []
    n = len(pos_dict)
    genes_processed_list.append(n)
    #print("counta_3", len(counta_3))
    #print("counta_5", len(counta_5))
    #print("unannotated", len(unannoated_nc_hits))
    avg_length = np.average(lengths)
    bin_size = avg_length/nbins
    bin_sizes.append(bin_size)
    utr_dict.update({ "5'_UTR" : (len(counta_5)*bin_size/1000)})
    utr_dict.update({ "3'_UTR" : (len(counta_3)*bin_size/1000)})
    hist_df = pd.DataFrame.from_dict(data = histogram_dict, orient="index")
    hist_df.reset_index(inplace=True)
    #hist_df["Histogram"] = hist_df.values.to_list()
    names = [i for i in range(1,nbins+1)]
    names.insert(0, "GeneID")
    hist_df.columns = names
    #print(hist_df.head(5))
    #hist_df.to_csv(sample+"_gene_histograms.txt", sep="\t", header = [i for i in range(1,nbins+1)], index=False)


    utr_labels = [k for k in utr_dict.keys()]
    utr_values = [v for v in utr_dict.values()]

    avg_hist = np.average(hist_over_all_genes, axis=0)
    avg_hist_list = avg_hist.tolist()
    bins = [j for j in range(1, len(avg_hist_list)+1)]
    
    plt.style.use("ggplot")
    plt.ylabel("Frequency per Bin")
    plt.xlabel("Bins")
    plt.xlim([-1,len(bins)])
    plt.xticks(fontsize = 7, rotation = 90, ha="center", weight = 'bold')
    plt.semilogy(bins, avg_hist_list)
    plt.savefig(file+"_SNV_graph.jpg")
    plt.close()
    total_hists.append(avg_hist_list)

    stat_writer.writerow({"Chr": file, "#Unannotated Hits": len(nc_list), "#Genes Processed": n})

    return()


##
TMP_DIR = sample+"_tmp/"
tmp_path = os.path.join(OUT_DIR, TMP_DIR)
try:
    os.mkdir(tmp_path)
except FileExistsError:
    pass

##split initial data file by chromosome number
with open(infile) as datafile:
    data_reader = pd.read_csv(infile, sep= "\t", header = 0)

for chr_no in range (1, chr_no+1):
    filename = data_reader[data_reader["Region"] == chr_no]
    if chr_no <= 9:
        filename.to_csv(tmp_path+sample+"chr"+str(0)+str(chr_no)+".txt", index = False, sep= '\t')
    else:
        filename.to_csv(tmp_path+sample+"chr"+str(chr_no)+".txt", index = False, sep= '\t')

##run stack_genes on the split files
with open(OUT_DIR+sample+"stats_file.txt", "a", newline="") as stats:
    fields = ["Chr","#Unannotated Hits", "#Genes Processed"]
    stat_writer = csv.DictWriter(stats, fieldnames= fields, delimiter = "\t")
    stat_writer.writeheader()

    for chr_file in os.listdir(tmp_path):
        data_file = os.path.join(tmp_path,chr_file)
        stack_genes(data_file, nbins, gtf)

avg_total_hist = np.average(total_hists, axis=0)
avg_total_hist_list = avg_total_hist.tolist()
bins = [i for i in range(1, (len(avg_total_hist)+1))]
bins[0] = "TSS"
bins[len(bins)-1] = "TTS"


## plotting
plt.style.use("ggplot")
plt.figure(figsize = (20, 7))
sns.barplot(x = bins, y = avg_total_hist_list, ci="sd", color="darkslateblue")
plt.errorbar(x = [str(i) for i in bins], y = avg_total_hist_list, yerr = np.std(total_hists, axis=0), ecolor="darkorange", elinewidth=1.5)
#plt.semilogy(bins, avg_total_hist_list, "-")
plt.title("SNV Distribution on Averaged Gene Body"+" ("+sample+")")
plt.ylabel("Frequency per Bin")
plt.xlabel("Bins")
plt.xlim([-1,len(bins)])
plt.xticks(fontsize = 8, rotation = 90, ha="center", weight = 'bold')
plt.savefig(OUT_DIR+"/"+sample+"_SNV_graph.jpg")
#plt.show()

##tabular record of plot data
plot_data = dict(zip(bins, avg_total_hist_list))
plot_df = pd.DataFrame.from_dict(data = plot_data, orient="index")
plot_df.reset_index(inplace=True)
plot_df.columns = ["Bin", "Freq"]
plot_df.to_csv(OUT_DIR+"/"+sample+"plot_data.txt", sep="\t", header = True, index = False)


