import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--infile", help="Input file containing SNV data")
parser.add_argument("-s", "--sample", help="The name of the sample (will be applied to any output files)")
parser.add_argument("-o", "--outpath", help="Folder where output heatmaps will be generated")
args = parser.parse_args()
sample = args.sample
infile = args.infile
outpath = args.outpath
out = os.path.abspath(outpath)

spans = pd.read_csv(infile, sep="\t", header=None)
#print(spans.head(5))

loci = []
nuc = []
for i in spans[0]:
    if (">") in i:
        loci.append(i)
    else:
        nuc.append(i)

print(len(loci))
print(len(nuc))

def typify(s):
    mid_index = int((len(s)-1)/2)
    focal = s[mid_index]
    front = s[0:mid_index]
    back = s[(mid_index+1):]
    return(focal+":"+front+"-"+back)

span_dict = dict(zip(loci, nuc))
#print(span_dict)
span_df = pd.DataFrame.from_dict(span_dict, orient="index")
span_df.reset_index(inplace=True)
span_df.columns = ["Coordinate", "Span"]
#print(span_df.head(5))

span_df["Focal:Flank"] = span_df.apply(lambda row : typify(row["Span"]), axis = 1)
delt, flank = np.unique(span_df["Focal:Flank"], return_counts= True)
del_dict = dict(zip(delt, flank))
#print(span_df.head(5))
#print(del_dict)
del_df = pd.DataFrame.from_dict(del_dict, orient="index")
del_df.reset_index(inplace=True)
del_df.columns = ["Focal:Flank", "Count"]

#print(del_df.head(5))

del_df[["Focal", "Flank"]] = del_df["Focal:Flank"].str.split(":", n = 1, expand = True)
#print(del_df.head(5))

ax = plt.axes()
ax.set_facecolor("cornflowerblue")
subset = del_df[del_df["Count"] >= 150]
sub_map = subset.pivot("Flank", "Focal", "Count")
sns.heatmap(sub_map, vmin=0, vmax=800, linewidths=.5, cmap = "icefire", annot=True, fmt="n", annot_kws={"fontsize":6}, yticklabels=1)
plt.savefig(out+"/"+sample+"_spans.svg", format="svg")
plt.savefig(out+"/"+sample+"_spans.png", format="png")
#plt.show()

## done, hopefully
