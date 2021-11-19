import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("ggplot")
mpl.rcParams["xtick.color"] = "black"
mpl.rcParams["ytick.color"] = "black"

effectsRaw = pd.read_csv("/Users/bruhaddave/Desktop/SNV_Rates/RevCommentsStuff/revisedOutputs/plot.Data/fig2C_FunctionalAnnotation/STable-9B-Functional Annotation-%.tsv", sep = "\t", header = 0)
effects = pd.melt(effectsRaw, id_vars = "Sample", var_name = "Effect", value_name = "Percent")
effects["Sample"] = effects["Sample"] = effects["Sample"].map(lambda x: x.removesuffix("_r1").removesuffix("_r2").removesuffix("_r3").lstrip("PF"))
effects["Effect"] = effects["Effect"].map(lambda x: x.lstrip('%'))

sns.barplot(data=effects, x = "Effect", y = "Percent", hue = "Sample", palette = "icefire", errwidth=1.5, capsize=0.03, errcolor="black", edgecolor = "0.2")
plt.xlabel("Predicted Effects", color = "k")
plt.ylabel("Proportion(%)", color = "k")
plt.tick_params(axis="x", labelsize = 9)
plt.xticks(ha="center", ticks=[0,1,2,3,4,5,6,7,8],labels=["UTR\nVariant", "Intronic\nVariant", "Missense\nVariant", "ncRNA\nVariant", "Splice\nVariant", "Start\nLost", "Stop\nGained", "Stop\nLost",  "Synonymous\nVariant"])
plt.title("Functional Annotation of SNVs Found in $\it{P. falciparum}$")
#plt.savefig("./example_plots/pfal_recoding_effects.svg", format="svg")
#plt.savefig("./example_plots/pfal_recoding_effects.png", format="png")
plt.show()