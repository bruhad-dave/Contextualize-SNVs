import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("ggplot")
mpl.rcParams["xtick.color"] = "black"
mpl.rcParams["ytick.color"] = "black"

to_fromRaw = pd.read_csv("/Users/bruhaddave/Desktop/SNV_Rates/RevCommentsStuff/revisedOutputs/plot.Data/fig2B_BaseShiftPatterns/STable-7B-baseShiftPatterns-%.tsv", sep = "\t", header = 0)
to_from = pd.melt(to_fromRaw, id_vars = "Sample", var_name = "Type", value_name = "Percent")
to_from["Sample"] = to_from["Sample"] = to_from["Sample"].map(lambda x: x.removesuffix("r1").removesuffix("r2").removesuffix("r3").lstrip("Pf"))
to_from["Type"] = to_from["Type"].map(lambda x: x.lstrip('%'))
#print(to_from.head())
new_index = ["A>", "T>", "G>", "C>", ">A", ">T", ">G", ">C"]
to_from = to_from.set_index("Type").loc[new_index].reset_index()

sns.barplot(data = to_from, x="Type", y="Percent", hue="Sample", palette="viridis_r", errwidth=1.5, capsize=0.03, errcolor="black", edgecolor = "0.2")
plt.xlabel("Nucleotide Shift (To = >N; From = N>)", color = "k")
plt.ylabel("Proportion(%)", color = "k")
plt.title("Base Shift Patterns in $\it{P. falciparum}$")
#plt.savefig("./example_plots/pfal_base_shift_patterns.svg", format="svg")
#plt.savefig("./example_plots/pfal_base_shift_patterns.png", format="png")
plt.show()