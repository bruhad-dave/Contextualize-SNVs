import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("ggplot")
mpl.rcParams["xtick.color"] = "black"
mpl.rcParams["ytick.color"] = "black"

sppRates = pd.read_csv("/Users/bruhaddave/Desktop/SNV_Rates/RevCommentsStuff/revisedOutputs/plot.Data/fig4_SppRates/spp_rates.tsv", sep = "\t", header = 0)
sns.barplot(data=sppRates, x = "Rate", y = "Sample", hue="Key", orient="horizontal", palette="viridis", errcolor="black", errwidth=1.5, capsize=0.1, edgecolor = "0.2")
plt.xlabel("SNV Rates (per kb)", color = "k")
plt.ylabel("Species", color = "k")
plt.yticks(ha="right", ticks=[0,1,2,3,4,5,6,7,8,9,10,11],labels=["PfMRA_1236", "PfMRA_1240", "PfMRA_1241", "Pf3D7_CTRL", "Pf3D7_TEMP", "Pf3D7_ART", "Pf_Mali\nIsolate", "Pv_liver\nMixed Culture", "Pv_liver\nHypnozoites", "Pv_simian\nBlood Stages", "E_coli", "B_subtilis"])
plt.tick_params(axis="y", labelsize = 6)
#plt.savefig("./example_plots/Figure4,1.svg", format="svg")
plt.show()