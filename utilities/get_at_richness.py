import Bio.SeqIO as bseq
import pandas as pd

## the reference file containing fasta records of all coding sequences.
reference = input("CDS fasta file (absolute path): ")

## function to count the number of As and Ts in a string
def counter(s):
    count = 0
    for i in range(len(s)):
        if s[i] == "A" or s[i] == "T":
            count += 1
    return(count)

at_dict = {}
## use the "counter function and append counts to a dictionary where key=name of fasta record and values are number of As/Ts, length of fasta record, and %AT-richness
with open(reference) as ref:
    for record in bseq.parse(ref, "fasta"):
        at_richness = counter(record)
        #print(record.id, at_richness, len(record), (at_richness*100)/len(record))
        at_dict[record.id] = at_richness, len(record), (at_richness*100)/len(record)

## convert at_dict to a dataframe and output as TSV. This TSV only needs to be made once for any given set of references and can be used every time AT-richness information is needed
at_df = pd.DataFrame.from_dict(at_dict, orient="index")
at_df.reset_index(inplace=True)
at_df.columns = ["TranscriptID", "AT_richness", "Length", "Percent_AT_Richness"]
print(at_df.head(5))

at_df.to_csv("at_richness.tsv", sep = "\t", index = False)

##done, hopefully
