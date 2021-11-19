import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

sfig1_raw = pd.read_csv("/Users/bruhaddave/Desktop/SNV_Rates/RevCommentsStuff/revisedOutputs/plot.Data/supplFig1.2.3/dnacovFilter.txt", sep = "\t", header = 0)
sfig2_raw = pd.read_csv("/Users/bruhaddave/Desktop/SNV_Rates/RevCommentsStuff/revisedOutputs/plot.Data/supplFig1.2.3/rnacovFilter.txt", sep = "\t", header = 0)
sfig3_raw = pd.read_csv("/Users/bruhaddave/Desktop/SNV_Rates/RevCommentsStuff/revisedOutputs/plot.Data/supplFig1.2.3/freqFilter.txt", sep = "\t", header = 0)
#print(sfig1_raw.head())
sfig1 = pd.melt(sfig1_raw, id_vars = "Sample", var_name = "dnacov_cutoff", value_name = "NumHits")
sfig2 = pd.melt(sfig2_raw, id_vars = "Sample", var_name = "rnacov_cutoff", value_name = "NumHits")
sfig3 = pd.melt(sfig3_raw, id_vars = "Sample", var_name = "freq_cutoff", value_name = "NumHits")
#print(sfig1.head())
sfig1["dnacov_cutoff"] = sfig1["dnacov_cutoff"].map(lambda x: x.lstrip("DNAcov"))
sfig2["rnacov_cutoff"] = sfig2["rnacov_cutoff"].map(lambda x: x.lstrip("RNAcov"))
sfig3["freq_cutoff"] = sfig3["freq_cutoff"].map(lambda x: x.lstrip("F"))

plt.style.use("ggplot")
mpl.rcParams["xtick.color"] = "black"
mpl.rcParams["ytick.color"] = "black"

sns.lineplot(data = sfig1, x = "dnacov_cutoff", y = "NumHits", hue = "Sample", style = "Sample", markers = ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], dashes = False)
plt.xlabel("DNA Coverage Cutoffs", color = "k")
plt.ylabel("Number of Hits Retained", color = "k")
plt.xticks(rotation = 25, ha = "right", fontsize = 9)
plt.show()

sns.lineplot(data = sfig2, x = "rnacov_cutoff", y = "NumHits", hue = "Sample", style = "Sample", markers = ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], dashes = False)
plt.xlabel("RNA Coverage Cutoffs", color = "k")
plt.ylabel("Number of Hits Retained", color = "k")
plt.xticks(rotation = 25, ha = "right", fontsize = 9)
plt.show()

sns.lineplot(data = sfig3, x = "freq_cutoff", y = "NumHits", hue = "Sample", style = "Sample", markers = ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], dashes = False)
plt.xlabel("Frequency Cutoffs", color = "k")
plt.ylabel("Number of Hits Retained", color = "k")
plt.xticks(rotation = 25, ha = "right", fontsize = 9)
plt.show()
