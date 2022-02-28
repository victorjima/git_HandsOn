#!/usr/bin/env python

import sys, re # import the system to establish arguments when running the script and search with re
from argparse import ArgumentParser # to create arguments

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA') # the help message
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence") # argument for sequence
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif") # argument for motif

if len(sys.argv) == 1: # if only the name of the script is called, the help message appears
    parser.print_help()
    sys.exit(1)

args = parser.parse_args() # define the variable for the arguments

args.seq = args.seq.upper()  # transform the sequence into capital letters
if re.search('^[ACGTU]+$', args.seq): # search for all the letters in the sequence
    if re.search('^[ACGT]+$', args.seq): 
        print ('The sequence is DNA') # if it contains a T the sequence is DNA
    elif re.search('^[ACGU]+$', args.seq):
        print ('The sequence is RNA') # if it contains a U the sequence is RNA
    else:
        print ('Ambiguity: the sequence may be either DNA or RNA') # if it contains both, either
else:
    print ('The sequence is neither DNA nor RNA') # not identified

if args.motif:
    args.motif = args.motif.upper() # transform motif to capital letters
    print("Motif search enabled: looking for motif in sequence...") # message that it is running
    if re.search(args.motif, args.seq): 
        print(f"Motif {args.motif}  is found in sequence {args.seq}") # if the motif is found
    else:
        print(f"Motif {args.motif} is not found in sequence {args.seq}")
