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
from learnchars.chars import get_next_character
from learnchars.hsk import HSK


def find_words_for_char(next_char):
    hsk = HSK()

    # Find first N words containing this character:
    found_words = []
    for word in wordfreq.iter_wordlist('zh'):
        if next_char in word:
            found_words.append(word)

        if len(found_words) == args.words:
            break

    # Print the words, their frequency, and HSK level (if applicable)
    for idx, word in enumerate(found_words):
        frequency = wordfreq.word_frequency(word, "zh")
        hsk_level = hsk.hsk_level(word)
        if hsk_level is not None:
            hsk_str = "HSK {}".format(hsk_level)
        else:
            hsk_str = ""

        print("{:<8}\t{:<8}\t{:<10}\t{}".format(idx, word, frequency, hsk_str))


if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Generate a list of vocabulary words to learn')
    p.add_argument('filename', type=Path, metavar='filename.tsv', help='path to Skritter tsv')
    p.add_argument('n', type=int, nargs='?', default=1, help='# new characters to learn')
    p.add_argument('-w', '--words', type=int, default=5, help='# words for each character')
    p.add_argument('-c', '--char', type=str, default='', help='character[s] to use for  words')
    args = p.parse_args()

    if not args.filename.is_file():
        sys.exit("Path to vocabulary list does not exist or is not a file")

    if args.n < 1:
        sys.exit("n must be >= 1")

    if args.words < 0:
        sys.exit("words must be >= 0")

    # Import vocabulary list
    vocab = Skritter(args.filename)

    if len(args.char) > 0:
        print("Words containing {}:".format(args.char))
        find_words_for_char(args.char)
    else:
        # Find [n] unknown characters and [words] new words per character
        next_chars = get_next_character(vocab.chars, args.n)
        for (next_char, rank) in next_chars:
            print("Next unknown character: {} (rank: {})".format(next_char, rank))
            find_words_for_char(next_char)
