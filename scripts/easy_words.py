#!/usr/bin/env python
"""
- Import known words from word list exported from Skritter.
- Get next most common unknown character from Jun Da's list
- Print five most common words containing that character from wordfreq
"""
import sys
import argparse
import wordfreq
from pathlib import Path
from learnchars.skritter import Skritter
from learnchars.hsk import HSK


def easy_to_learn(word, known_chars):
    for c in word:
        if c not in known_chars:
            return False

    return True


if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Generate a list of vocabulary words to learn')
    p.add_argument('filename', type=Path, metavar='filename.tsv', help='path to Skritter tsv')
    args = p.parse_args()

    if not args.filename.is_file():
        sys.exit("Path to vocabulary list does not exist or is not a file")

    # Import vocabulary list, load HSK lists
    vocab = Skritter(args.filename)
    hsk = HSK()

    # Find words that are composed entirely of characters I know
    for word in wordfreq.iter_wordlist('zh'):
        # Skip words I already know
        if word in vocab.words:
            continue

        # Skip words which contain characters I don't know
        if not easy_to_learn(word, vocab.chars):
            continue

        # Print word and HSK level
        print("{:<10}\tHSK {}".format(word, hsk.hsk_level(word)))
