import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--infile", help="Input file containing plot data (get_freq_v2.py output)")
parser.add_argument("-n", "--name", help="The name to assign to the output.")
args = parser.parse_args()

inFile = args.infile
sample = args.name

plt.style.use("ggplot")
mpl.rcParams["xtick.color"] = "black"
mpl.rcParams["ytick.color"] = "black"

data = pd.read_csv(inFile, sep = "\t", header = 0)
data["TPM"] = data["TPM"] + 1
data["logTPM"] = np.log(data["TPM"])
## log10(TPM) v/s SNV SumFreq
corr = "r = "+str(data["logTPM"].corr(data["SumFreq"]).round(2))
sns.scatterplot(data = data, x = "logTPM", y = "SumFreq")
plt.xlabel("Gene Expression: ln(TPM+1)", color = "k")
plt.ylabel("Sum of SNV Frequencies\nOver Variant Loci", color = "k")
plt.text(x=max(data["logTPM"])-1, y = max(data["SumFreq"])-1, s = corr, weight = "bold")
plt.title(sample, color = "k")
plt.savefig(sample+"_logTPM.SumFreq.jpeg")
plt.savefig(sample+"_logTPM.SumFreq.svg")
plt.close()
#plt.show()

sns.scatterplot(data = data, x = "%AT_Richness", y = "SumFreq")
corr1 = "r = "+str(data["%AT_Richness"].corr(data["SumFreq"]).round(2))
plt.xlabel("A-T Content (%)", color = "k")
plt.ylabel("Sum of SNV Frequencies\nOver Variant Loci", color = "k")
plt.text(x=min(data["%AT_Richness"])+0.25, y = max(data["SumFreq"])-1, s = corr1, weight = "bold")
plt.title(sample, color = "k")
plt.savefig(sample+"_atRich.SumFreq.jpeg")
plt.savefig(sample+"_atRich.SumFreq.svg")
plt.close()
#plt.show()