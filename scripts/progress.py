#!/usr/bin/env python
"""
Display a summary of learning progress for the N most frequent characters
"""
import sys
import argparse
from pathlib import Path
from learnchars.skritter import Skritter
from learnchars.chars import display_progress


if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Summarize character learning progress')
    p.add_argument('filename', type=Path, metavar='filename.tsv', help='path to Skritter tsv')
    p.add_argument('n', type=int, nargs='?', default=1000, help='# characters to cover')
    p.add_argument('-i', '--invert', action='store_true', help='display unknown characters')
    args = p.parse_args()

    if not args.filename.is_file():
        sys.exit("Path to vocabulary list does not exist or is not a file")

    if args.n < 1:
        sys.exit("n must be >= 1")

    # Import vocabulary list
    vocab = Skritter(args.filename)
    percent = display_progress(vocab.chars, args.n, args.invert)
    print("Known: {:0.2f}".format(percent))
