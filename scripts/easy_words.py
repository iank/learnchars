#!/usr/bin/env python
import sys
import argparse
import wordfreq
from pathlib import Path
from learnchars.skritter import Skritter
from learnchars.hsk import HSK
from learnchars.cedict import CEDICT
from signal import signal, SIGPIPE, SIG_DFL


def easy_to_learn(word, known_chars):
    for c in word:
        if c not in known_chars:
            return False

    return True


if __name__ == '__main__':
    signal(SIGPIPE, SIG_DFL)
    p = argparse.ArgumentParser(description='Generate a list of vocabulary words to learn')
    p.add_argument('filename', type=Path, metavar='filename.tsv', help='path to Skritter tsv')
    args = p.parse_args()

    if not args.filename.is_file():
        sys.exit("Path to vocabulary list does not exist or is not a file")

    # Import vocabulary list, load HSK lists, CEDICT
    vocab = Skritter(args.filename)
    hsk = HSK()
    cedict = CEDICT()

    # Find words that are composed entirely of characters I know
    for word in wordfreq.iter_wordlist('zh'):
        # Skip words I already know
        if word in vocab.words:
            continue

        # Skip words which contain characters I don't know
        if not easy_to_learn(word, vocab.chars):
            continue

        # Print word and HSK level
        entry = cedict.lookup(word)
        if entry is not None:
            meaning = entry.meanings[0]
        else:
            meaning = ""

        print("{:<10}\tHSK {}\t{}".format(word, hsk.hsk_level(word), meaning))
