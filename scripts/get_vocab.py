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
from learnchars.skritter import import_from_tsv
from learnchars.chars import get_next_character

if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Generate a list of vocabulary words to learn')
    p.add_argument('filename', type=Path, metavar='filename.tsv', help='path to Skritter tsv')
    p.add_argument('n', type=int, nargs='?', default=1, help='# new characters to learn')
    p.add_argument('-w', '--words', type=int, default=5, help='# words for each character')
    args = p.parse_args()

    if not args.filename.is_file():
        sys.exit("Path to vocabulary list does not exist or is not a file")

    if args.n < 1:
        sys.exit("n must be >= 1")

    if args.words < 0:
        sys.exit("words must be >= 0")

    # Import vocabulary list
    chars = import_from_tsv(args.filename)

    # Find [n] unknown characters and [words] new words per character
    next_chars = get_next_character(chars, args.n)
    for (next_char, rank) in next_chars:
        print("Next unknown character: {} (rank: {})".format(next_char, rank))

        found_words = 0
        for word in wordfreq.iter_wordlist('zh'):
            if next_char in word:
                found_words = found_words + 1
                print("#{}:\t{}\t({})".format(
                    found_words, word, wordfreq.word_frequency(word, "zh"))
                )

            if found_words == args.words:
                break
