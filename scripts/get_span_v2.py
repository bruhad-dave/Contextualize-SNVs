## this version of get_span outputs two files, including a <name>.span_data_file.txt that records strand info and feeds into get_span_strcorr.py
import pandas as pd
import argparse

## arguments
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--spanlen", type=int, help="The number of nucleotides to extract")
parser.add_argument("-i", "--infile", help="Input file containing SNV data")
parser.add_argument("-s", "--sample", help="The name of the sample (will be applied to any output files)")
args = parser.parse_args()
span = args.spanlen
sample = args.sample
infile = args.infile

def get_span_coords(chrom, position, span_length):
    start = position - span_length
    end = position + span_length
    return str(chrom)+":"+str(start)+"-"+str(end)

data = pd.read_csv(infile, sep = "\t", header = 0)
data = data[["Region", "Position", "Reference", "Strand"]]
data["Span_Coordinates"] = data.apply(lambda row : get_span_coords(row["Region"], row["Position"], span), axis = 1)

data.to_csv("./"+sample+".span_data_file.txt", index = False, header = True, sep = "\t")
span_df = data[["Span_Coordinates"]]
span_df.to_csv("./"+sample+".span_file.txt", index = False, header = False, sep = "\t")
