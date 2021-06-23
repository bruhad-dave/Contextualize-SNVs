import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

## NOTE: filenames below are placeholders
at_ref = "at_richness_file.tsv" ## at_richness file as generated using get_at_richness.py
names = "geneIDs_transcriptIDs.txt" ## tab-separated file containing gene IDs and corresponding transcript IDs
data_file = "sample.get_freq.txt" ## input file as generated using get_freq.py
exp_file = "sample_quant.sf" ## raw gene abundance counts file generated using Salmon (https://salmon.readthedocs.io/en/latest/salmon.html)

at = pd.read_csv(at_ref, sep="\t", header=0)
names_df = pd.read_csv(names, sep="\t", header=0)
data_df = pd.read_csv(data_file, sep="\t", header=0)
exp_df = pd.read_csv(exp_file, sep="\t", usecols=["Name", "TPM"])

at_names = pd.merge(at, names_df, left_on="TranscriptID", right_on="cDNA_ID")
#print(at_names.head(5))
merged = pd.merge(at_names, data_df, on="GeneID")
#print(merged.head(5))

merged_exp = pd.merge(merged, exp_df, left_on="cDNA_ID", right_on="Name")
#print(merged_exp.head(5))

cleaned_1 = merged_exp[["TranscriptID", "AT_richness", "Percent_AT_Richness", "Length", "Relative_Freq([1]/[2])", "TPM"]]
cleaned = cleaned_1[cleaned_1["TPM"] > 0]
#print(cleaned.head(5))
plt.style.use("ggplot")
sns.scatterplot(x=cleaned["Percent_AT_Richness"], y=cleaned["Relative_Freq([1]/[2])"])
#m, b = np.polyfit(cleaned["Percent_AT_Richness"], cleaned["Relative_Freq([1]/[2])"], 1)
#print(m)
#plt.plot(cleaned["Percent_AT_Richness"], m*cleaned["Percent_AT_Richness"]+b, "-k")
plt.xlabel("% AT-Content", color = "k")
plt.ylabel("Relative SNV Frequency", color = "k")
#plt.show()
plt.savefig("AT_sample.svg") ## Placeholder filepath
plt.close()

plt.style.use("ggplot")
sns.scatterplot(x=cleaned["TPM"], y=cleaned["Relative_Freq([1]/[2])"])
plt.xlabel("TPM", color = "k")
plt.ylabel("Relative SNV Frequency", color = "k")
#plt.show()
plt.savefig("tpm__sample.svg") ## Placeholder filepath
plt.close()

## the lines below print out Pearson's correlation coefficients for the respective sets of values
print(cleaned["Percent_AT_Richness"].corr(cleaned["Relative_Freq([1]/[2])"]))
print(cleaned["TPM"].corr(cleaned["Relative_Freq([1]/[2])"]))

## done, hopefully
