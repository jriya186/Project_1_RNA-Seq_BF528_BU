#!/usr/bin/env python3

import pandas as pd
import argparse
import os

# Argument parser to handle input files and output file
parser = argparse.ArgumentParser(description="Merge VERSE output files into a counts matrix")
parser.add_argument("-i", "--input", nargs="+", required=True, help="List of VERSE output files")
parser.add_argument("-o", "--output", required=True, help="Output counts matrix file")
args = parser.parse_args()

# Read and concatenate all input files
dataframes = []

for file in args.input:
    sample_name = os.path.basename(file).replace("_counts.txt", "")
    df = pd.read_csv(file, sep="\t", header=None, names=["Gene", sample_name])
    df.set_index("Gene", inplace=True)
    dataframes.append(df)

# Merge all dataframes by Gene column
merged_df = pd.concat(dataframes, axis=1)

# Save the final counts matrix
merged_df.to_csv(args.output, sep="\t")

print(f"Successfully merged {len(args.input)} files into {args.output}")
