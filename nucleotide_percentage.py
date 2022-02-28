#!/usr/bin/env python

import sys, re # import the system to establish arguments when running the script
import pandas as pd # import pandas to display the output in a data frame
from argparse import ArgumentParser # to create arguments

parser = ArgumentParser(description = 'Given a DNA or RNA sequence, it computes the % of each nucleotide') # the help message
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence") # argument for sequence
parser.add_argument("-t", "--type", type = str, required = True, help = "Type of sequence: either DNA or RNA") # argument for the type of sequence

if len(sys.argv) == 1: # if only the name of the script is called, the help message appears
    parser.print_help()
    sys.exit(1)
    
args = parser.parse_args() # define the variable for the arguments

args.seq = args.seq.upper()  # transform the sequence into capital letters
args.type = args.type.upper()  # transform type of sequence into capital letters

if args.type == "DNA": # if type of sequence is RNA
    if re.search('^[ACGU]+$', args.seq): # check if sequence is RNA
        RNA_perc = [] # initialize list to contain percentages
        RNA_counts = [] # initialize lust to contain counts
        for char in "ACGU":
            RNA_counts.append(args.seq.count(char)) # compute total values for each character
            RNA_perc.append((args.seq.count(char)/len(args.seq))*100) # compute the percentage for each nucleotide and add to list
        percentage = pd.DataFrame({"Counts":RNA_counts, "Percentage (%)":RNA_perc}) # put the counts and percentages in the dataframe
        percentage.index = ["A", "C", "G", "U"] # row names
        print(percentage)
    else:
        print("Type of sequence does not match the content of the sequence") # if sequence is not really RNA
elif args.type == "RNA": # if type of sequence is DNA
     if re.search('^[ACGT]+$', args.seq): # check if sequence is DNA
        DNA_perc = [] # initialize list to contain percentages
        DNA_counts = [] # initialize lust to contain counts
        for char in "ACGT":
            DNA_counts.append(args.seq.count(char)) # compute total values for each character
            DNA_perc.append((args.seq.count(char)/len(args.seq))*100) # compute the percentage for each nucleotide and add to list
        percentage = pd.DataFrame({"Counts":DNA_counts, "Percentage (%)":DNA_perc}) # put the counts and percentages in the dataframe
        percentage.index = ["A", "C", "G", "T"] # row names
        print(percentage)    
     else:
        print("Type of sequence does not match the content of the sequence") # if sequence is not really RNA
else:
    print("Sequence type is not identified")
