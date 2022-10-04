#!/usr/bin/env python
"""
- Import known words from word list exported from Skritter.
- Import a text file and count character frequency (not word frequency, use CTA for that)
- List known/unknown characters by frequency
"""
import sys
import argparse
from pathlib import Path
from learnchars.skritter import import_from_tsv
from learnchars.textfile import analyze_frequency

if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Analyze text by characters')
    p.add_argument('filename', type=Path, metavar='filename.tsv', help='path to Skritter tsv')
    p.add_argument('textfile', type=Path, metavar='textfile.txt', help='path to text file')
    p.add_argument('-k', '--known', help='include known characters', action='store_true')
    args = p.parse_args()

    if not args.filename.is_file():
        sys.exit("Path to vocabulary list does not exist or is not a file")
    if not args.textfile.is_file():
        sys.exit("Path to vocabulary list does not exist or is not a file")

    # Import vocabulary list
    chars = import_from_tsv(args.filename)

    # Analyze text file
    textchars = analyze_frequency(args.textfile)

    print("character: count")
    for char, count in textchars.items():
        if char in chars:
            if args.known:
                print("#{}: {}".format(char, count))
        else:
            print(" {}: {}".format(char, count))
