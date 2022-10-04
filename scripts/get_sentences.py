#!/usr/bin/env python
import sys
import argparse
import zhon.hanzi
import string
from pathlib import Path
from learnchars.skritter import import_from_tsv


def sentence_known(sentence, chars):
    for c in sentence:
        if c not in chars:
            return False

    return True


if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Get some sentences')
    p.add_argument('filename', type=Path, metavar='filename.tsv', help='path to Skritter tsv')
    p.add_argument('sentences', type=Path, metavar='sentences.tsv', help='sentences tsv')
    p.add_argument('-c', '--chars', type=str, default='',
                   help='string containing additional characters to include')
    args = p.parse_args()

    if not args.filename.is_file():
        sys.exit("Path to vocabulary list does not exist or is not a file")
    if not args.sentences.is_file():
        sys.exit("Path to sentences does not exist or is not a file")

    # Import vocabulary list
    chars = import_from_tsv(args.filename)
    chars |= set(zhon.hanzi.punctuation)
    chars |= set(string.whitespace)
    chars |= set(args.chars)

    sentences = []
    with open(args.sentences) as f:
        for line in f:
            (sentence, pinyin, translation) = line.split('\t')
            translation = translation.rstrip()
            if sentence_known(sentence, chars):
                sentences.append(sentence)
                print("{} - {} - {}".format(sentence, pinyin, translation))
