#!/usr/bin/env python3

import argparse

def parse_gtf(gtf_file, output_file):
    """
    Parses a GTF file and extracts Ensembl gene IDs and gene names.

    Args:
        gtf_file (str): Path to the input GTF file.
        output_file (str): Path to the output text file.
    """
    with open(gtf_file, 'r') as gtf, open(output_file, 'w') as out:
        out.write("Ensembl_ID\tGene_Name\n")  # Write header
        for line in gtf:
            if line.startswith("#"):
                continue  # Skip comment lines
            columns = line.strip().split("\t")
            if columns[2] == "gene":
                attributes = {}
                for attr in columns[8].split(";"):
                    attr = attr.strip()
                    if " " in attr:  # Ensure valid key-value pairs
                        key, value = attr.split(" ", 1)  # Split only on first space
                        attributes[key.strip()] = value.strip('"')
                
                ensembl_id = attributes.get("gene_id", "NA")
                gene_name = attributes.get("gene_name", "NA")
                out.write(f"{ensembl_id}\t{gene_name}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse a GTF file and extract Ensembl gene IDs and gene names.")
    parser.add_argument("-i", "--input", required=True, help="Path to the input GTF file")
    parser.add_argument("-o", "--output", required=True, help="Path to the output file")

    args = parser.parse_args()
    parse_gtf(args.input, args.output)