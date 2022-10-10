#!/usr/bin/env python
"""
- Import known words from word list exported from Skritter.
- Import a text file and count character frequency (not word frequency, use CTA for that)
- List known/unknown characters by frequency

- Calculate characters that would be needed for X% character recognition
"""
import sys
import argparse
import math
from pathlib import Path
from learnchars.skritter import Skritter
from learnchars.textfile import analyze_frequency
from learnchars.textfile import count_characters
from learnchars.chars import get_character_rank

if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Analyze text by characters')
    p.add_argument('filename', type=Path, metavar='filename.tsv', help='path to Skritter tsv')
    p.add_argument('textfile', type=Path, metavar='textfile.txt', help='path to text file')

    p.add_argument('-p', '--percent', type=float,
                   help='print characters needed to learn to reach X%% character coverage')
    args = p.parse_args()

    if not args.filename.is_file():
        sys.exit("Path to vocabulary list does not exist or is not a file")
    if not args.textfile.is_file():
        sys.exit("Path to vocabulary list does not exist or is not a file")

    # Import vocabulary list
    vocab = Skritter(args.filename)

    # Analyze text file
    textchars = analyze_frequency(args.textfile)

    # If we just want a list of known/unknown characters in the text
    if not args.percent:
        print("character: count_in_this_text (Jun Da's rank)")
        for char, count in textchars.items():
            if char not in vocab.chars:
                print(" {}: {}".format(char, count))

    # Otherwise, show the characters that would be needed to learn in order to
    # reach args.percent% *character* coverage of the given text.
    else:
        if args.percent < 0 or args.percent > 1:
            sys.exit("percent should be between 0-1 (inclusive)")

        charcount = count_characters(args.textfile)
        must_know = math.ceil(charcount * args.percent)

        print("Input file contains {} total characters".format(charcount))
        print("For {:0.2f}% comprehension, you must know {}".format(
            args.percent * 100, must_know)
        )

        known_count = 0
        for char, count in textchars.items():
            if char in vocab.chars:
                known_count = known_count + count

        print("You currently know {}/{} ({:0.2f}%)".format(
            known_count, must_know, known_count / charcount * 100
        ))

        if known_count > must_know:
            sys.exit()

        must_know = must_know - known_count
        print("Characters to learn to reach {:0.2f}% character coverage".format(
            args.percent * 100
        ))
        print("character: count_in_this_text (Jun Da's rank)")
        for char, count in textchars.items():
            if must_know <= 0:
                break
            if char in vocab.chars:
                continue
            print(" {}: {} ({})".format(char, count, get_character_rank(char)))
            must_know = must_know - count
