import pandas as pd
import argparse
from pathlib import Path
from functools import reduce

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--first", help="Replicate 1")
parser.add_argument("-b", "--second", help="Replicate 2")
parser.add_argument("-c", "--third", help="REplicate 3 (if available)")
args = parser.parse_args()
file1 = args.first
file2 = args.second
file3 = args.third

def summarise(file):
    df = pd.read_csv(file, sep = "\t", header=0)
    df["Stat"] = df["Region"].astype(str)+df["Position"].astype(str)
    statList = df["Stat"].tolist()
    return statList

a = summarise(file1)
b = summarise(file2)
if file3 is not None:
    c = summarise(file3)

if file3:
    print("a=", len(a), "b=", len(b), "c=", len(c))
else:
    print("a=", len(a), "b=", len(b))
if file3:
    ab = list(set(a) & set(b))
    bc = list(set(b) & set(c))
    ac = list(set(a) & set(c))
    abc = list(set(ab) & set(c))
    print("ab=", len(ab), "bc=", len(bc), "ac=", len(ac), "abc=", len(abc))
elif not file3:
    ab = list(set(a) & set(b))
    print("ab=", len(ab))


