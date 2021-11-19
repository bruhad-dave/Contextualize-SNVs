import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("ggplot")
mpl.rcParams["xtick.color"] = "black"
mpl.rcParams["ytick.color"] = "black"

base_percentRaw = pd.read_csv("/Users/bruhaddave/Desktop/SNV_Rates/RevCommentsStuff/revisedOutputs/plot.Data/fig2A_BaseChangeSpectra/STable-6B-baseChangeSpectra-%.tsv", sep = "\t", header = 0)
#print(base_percentRaw.head())
base_percent = pd.melt(base_percentRaw, id_vars = "Sample", var_name = "Sub", value_name = "Percent")
#print(base_percent.head())
base_percent["Sample"] = base_percent["Sample"] = base_percent["Sample"].map(lambda x: x.removesuffix("r1").removesuffix("r2").removesuffix("r3").lstrip("Pf"))
base_percent["Sub"] = base_percent["Sub"].map(lambda x: x.lstrip('%'))
#print(base_percent.head())
sns.barplot(x = base_percent["Sub"], y = base_percent["Percent"], hue=base_percent["Sample"], dodge=True, palette="viridis_r", edgecolor = "0.2", errwidth=1.5, capsize= 0.03, errcolor="black")
plt.xlabel("Base Substitution", color = "k")
plt.ylabel("Proportion(%)", color = "k")
plt.title("The Spectrum of Base Changes in $\it{P. falciparum}$")
#plt.savefig("/Users/bruhaddave/Desktop/SNV_Rates/RevCommentsStuff/revisedOutputs/final.Figs/fig2A.svg", format="svg")
#plt.savefig("/Users/bruhaddave/Desktop/SNV_Rates/RevCommentsStuff/revisedOutputs/final.Figs/fig2A.png", format="png")
plt.show()
