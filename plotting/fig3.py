import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("ggplot")
mpl.rcParams["xtick.color"] = "black"
mpl.rcParams["ytick.color"] = "black"

rates = pd.read_csv("/Users/bruhaddave/Desktop/SNV_Rates/RevCommentsStuff/revisedOutputs/plot.Data/fig3_Rates/pf_rates.tsv", sep = "\t", header = 0)
rates["Sample"] = rates["Sample"].map(lambda x: x.removesuffix("r1").removesuffix("r2").removesuffix("r3"))


sns.barplot(rates["Sample"], rates["RatePerKB"], color= "midnightblue", errcolor= "black", capsize=0.1, errwidth=1.5, edgecolor = "0.2")
plt.hlines(y=2.1, xmin=0, xmax=3, linestyle = "-", color = "k")
plt.hlines(y=2.0, xmin=1, xmax=3, linestyle = "-", color = "k")
plt.hlines(y=1.9, xmin=3, xmax=5, linestyle = "-", color = "k")

plt.text(x=1.5, y=2.105, s="*", weight="bold")
plt.text(x=2, y=2.005, s="***", weight="bold")
plt.text(x=4, y=1.905, s="*", weight="bold")
##plt.text(x=3.5, y=1.805, s="*", weight="bold")
#plt.text(x=4.8, y=2, s= "p < 0.001", weight="bold")
plt.title("SNV Rate per kb ($\it{P. falciparum}$)")
plt.xlabel("Sample", color = "k")
plt.ylabel("SNV rate", color = "k")
plt.tick_params(axis="x", labelsize = 9)
#plt.savefig("./example_plots/pfal_rates.svg", format="svg")
plt.show()