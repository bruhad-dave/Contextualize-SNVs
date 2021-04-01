## importing
import csv
import argparse

##arguments
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--spanlen", type=int, help="The number of nucleotides to extract")
parser.add_argument("-i", "--infile", help="Input file containing SNV data")
parser.add_argument("-s", "--sample", help="The name of the sample (will be applied to any output files)")
args = parser.parse_args()
span = args.spanlen
sample = args.sample
infile = args.infile


## get snv spans; get chr:start-end
n = 0

tmp1 = "./"+str(sample)+".span_data_file.txt"
tmp2 = "./"+str(sample)+".span_file.txt"
with open(tmp1, "w", newline= "") as tmp_file:
    fieldnames = ["Chr#","SNV_Pos","START", "END", "SpanSeq"]
    tmp_writer = csv.DictWriter(tmp_file, fieldnames= fieldnames, delimiter = "\t")
    with open(infile, "r", newline= "") as snv_file:
        in_filereader = csv.DictReader(snv_file, delimiter = "\t")
        tmp_writer.writeheader()
        with open(tmp2, "w", newline= "") as outfile:
            out_writer = csv.DictWriter(outfile, fieldnames= ["Span"])
            #out_writer.writeheader()
            for row in in_filereader:
                chr_no = row["Region"]
                snv_pos = int(row["Position"])
                #print("Working on", "chr"+str(chr_no), "position "+str(snv_pos)+"...")
                n += 1
                span_start = snv_pos - span
                span_end = snv_pos + span
                tmp_writer.writerow({"Chr#": ("chr"+chr_no), "SpanSeq": (str(chr_no)+":"+str(span_start)+"-"+str(span_end)), "SNV_Pos": snv_pos, "START": span_start, "END": span_end})
                out_writer.writerow({"Span": (str(chr_no)+":"+str(span_start)+"-"+str(span_end))})

print("Analysed", n, "positions.")

tmp_file.close()
snv_file.close()
outfile.close()

## done, hopefully
