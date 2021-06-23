import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl

## NOTE: the filepaths below are placeholders
base_percent = pd.read_csv("percentage_base_changes.tsv", sep="\t", header=0)
to_from = pd.read_csv("base_shift_patterns.tsv", sep="\t", header=0)
rates = pd.read_csv("snv_rates.tsv", sep="\t", header=0)
effects = pd.read_csv("coding_effects.tsv", sep="\t", header=0)
species_rates = pd.read_csv("snv_rates_across_species.tsv", sep="\t", header=0, usecols=["Sample", "Rate(Pre-SNP Filter)", "Rate(Post-SNP Filter)"])

cm = 0.3937007874
plt.style.use("ggplot")
mpl.rcParams["xtick.color"] = "black"
mpl.rcParams["ytick.color"] = "black"
plt.figure(figsize=(21*cm,9.9*cm))

## RATES PLOT

#sns.barplot(rates["Sample"], rates["Rate per kb"], color= "midnightblue", errcolor= "black", capsize=0.1, errwidth=1.5, edgecolor = "0.2")
##plt.hlines(y=2.1, xmin=0, xmax=3, linestyle = "-", color = "k")
#plt.hlines(y=2.0, xmin=1, xmax=3, linestyle = "-", color = "k")
##plt.hlines(y=1.9, xmin=2, xmax=3, linestyle = "-", color = "k")
##plt.hlines(y=1.8, xmin=3, xmax=4, linestyle = "-", color = "k")
##plt.text(x=1.5, y=2.105, s="*", weight="bold")
#plt.text(x=2, y=2.005, s="*", weight="bold")
##plt.text(x=2.5, y=1.905, s="*", weight="bold")
##plt.text(x=3.5, y=1.805, s="*", weight="bold")
#plt.text(x=4.8, y=2, s= "p < 0.001", weight="bold")
#plt.title("SNV Rate per kb ($\it{P. falciparum}$)")
#plt.xlabel("Sample", color = "k")
#plt.ylabel("SNV rate", color = "k")
#plt.tick_params(axis="x", labelsize = 9)
#plt.savefig("./example_plots/pfal_rates.svg", format="svg")
#plt.show()

## PERCENT BASE CHANGE PLOT

#sns.barplot(x = base_percent["Sub"], y = base_percent["Percent"], hue=base_percent["Sample"], dodge=True, palette="viridis_r", edgecolor = "0.2", errwidth=1.5, capsize= 0.03, errcolor="black")
#plt.xlabel("Base Substitution", color = "k")
#plt.ylabel("Proportion(%)", color = "k")
#plt.title("The Spectrum of Base Changes in $\it{P. falciparum}$")
#plt.savefig("./example_plots/pfal_base_change.svg", format="svg")
#plt.savefig("./example_plots/pfal_base_change.png", format="png")
#plt.show()

## PERCENT BASE SHIFT PATTERNS PLOT

#sns.barplot(data = to_from, x="Type", y="Percent", hue="Sample", palette="viridis_r", errwidth=1.5, capsize=0.03, errcolor="black", edgecolor = "0.2")
#plt.xlabel("Nucleotide Shift (To = >N; From = N>)", color = "k")
#plt.ylabel("Proportion(%)", color = "k")
#plt.title("Base Shift Patterns in $\it{P. falciparum}$")
#plt.savefig("./example_plots/pfal_base_shift_patterns.svg", format="svg")
#plt.savefig("./example_plots/pfal_base_shift_patterns.png", format="png")
#plt.show()

## PERCENT PREDICTED EFFECTS COURSE

#sns.barplot(data=effects, x = "Effect", y = "Percent", hue = "Sample", palette = "icefire", errwidth=1.5, capsize=0.03, errcolor="black", edgecolor = "0.2")
#plt.xlabel("Predicted Effects", color = "k")
#plt.ylabel("Proportion(%)", color = "k")
#plt.tick_params(axis="x", labelsize = 9)
#plt.xticks(ha="center", ticks=[0,1,2,3,4,5,6,7,8],labels=["Missense\nVariant", "Synonymous\nVariant", "UTR\nVariant", "Stop\nGained", "Stop\nLost", "Start\nLost", "Intronic\nVariant", "ncRNA\nVariant", "Splice\nVariant"])
#plt.title("Functional Annotation of SNVs Found in $\it{P. falciparum}$")
#plt.savefig("./example_plots/pfal_recoding_effects.svg", format="svg")
#plt.savefig("./example_plots/pfal_recoding_effects.png", format="png")
#plt.show()

## SPECIES RATES PLOT

tidied_rates = pd.melt(species_rates, id_vars="Sample")
print(tidied_rates.head(5))
tidied_rates.columns = ["Sample", "Key", "Rate"]
sns.barplot(data=tidied_rates, x = "Rate", y = "Sample", hue="Key", orient="horizontal", palette="viridis", errcolor="black", errwidth=1.5, capsize=0.1, edgecolor = "0.2")
plt.xlabel("SNV Rates (per kb)", color = "k")
plt.ylabel("Species", color = "k")
plt.yticks(ha="right", ticks=[0,1,2,3,4,5,6,7,8,9,10,11],labels=["PF3D7_CTRL", "PF3D7_TEMP", "PF3D7_ART", "MRA_1236", "MRA_1240", "MRA_1241", "PF_Mali\nIsolate", "P_vivax\nMixed Culture", "P_vivax\nHypnozoites", "P_vivax\nBlood Stages", "E_coli", "B_subtilis"])
plt.tick_params(axis="y", labelsize = 6)
plt.savefig("./example_plots/Figure4,1.svg", format="svg")
plt.show()

## done, hopefully
