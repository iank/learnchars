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
from learnchars.chars import str_progress


def print_unknown_chars(textchars, vocab):
    """Print unknown characters in a given text"""
    print("character: count_in_this_text (Jun Da's rank)")
    for char, count in textchars.items():
        if char not in vocab.chars:
            print(" {}: {} ({})".format(char, count, get_character_rank(char)))


def print_needed_chars(textfile, percent, textchars, vocab):
    """Print a list of characters that would be needed to reach target coverage"""
    ret_list = []
    if percent < 0 or percent > 1:
        sys.exit("percent should be between 0-1 (inclusive)")

    charcount = count_characters(textfile)
    must_know = math.ceil(charcount * percent)

    print("Input file contains {} total characters".format(charcount))
    print("For {:0.2f}% comprehension, you must know {}".format(
        percent * 100, must_know)
    )

    known_count = 0
    for char, count in textchars.items():
        if char in vocab.chars:
            known_count = known_count + count

    print("You currently know {}/{} ({:0.2f}%)".format(
        known_count, charcount, known_count / charcount * 100
    ))

    if known_count > must_know:
        sys.exit()

    must_know = must_know - known_count
    print("Characters to learn to reach {:0.2f}% character coverage".format(
        percent * 100
    ))
    print("character: count_in_this_text (Jun Da's rank)")
    for char, count in textchars.items():
        if must_know <= 0:
            break
        if char in vocab.chars:
            continue
        print(" {}: {} ({})".format(char, count, get_character_rank(char)))
        ret_list.append(char)
        must_know = must_know - count

    return ret_list


def print_sorted_chars(textchars, vocab, threshold):
    textchars = {k: v for (k, v) in textchars.items() if k not in vocab.chars}
    tcs = {get_character_rank(k): k for (k, v) in textchars.items() if v != 1}
    print("character: count_in_this_text (Jun Da's rank)")
    for key in sorted(tcs):
        if key <= args.sort:
            print(" {}: {} ({})".format(tcs[key], textchars[tcs[key]], key))


if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Analyze text by characters')
    p.add_argument('filename', type=Path, metavar='filename.tsv', help='path to Skritter tsv')
    p.add_argument('textfile', type=Path, metavar='textfile.txt', help='path to text file')

    p.add_argument('-p', '--percent', type=float,
                   help='print characters needed to learn to reach X%% character coverage')
    p.add_argument('-H', '--highlight', action='store_true',
                   help='print progress display with unknown characters in text highlighted')
    p.add_argument('-s', '--sort', type=int,
                   help="Sort by Jun Da's character rank, not rank in text. "
                        + 'Only return characters with Jun Da rank less than or equal to SORT. '
                        + 'Also exclude characters with 1 occurrence in the text.')
    args = p.parse_args()

    if not args.filename.is_file():
        sys.exit("Path to vocabulary list does not exist or is not a file")
    if not args.textfile.is_file():
        sys.exit("Path to vocabulary list does not exist or is not a file")

    # FIXME i'm sure argparse can handle this
    if args.percent and args.sort:
        sys.exit("Choose one of [-p, -s]")
    if args.highlight and not args.percent:
        sys.exit("-H needs -p")

    # Import vocabulary list
    vocab = Skritter(args.filename)

    # Analyze text file
    textchars = analyze_frequency(args.textfile)

    # Show the characters that would be needed to learn in order to
    # reach args.percent% *character* coverage of the given text.
    if args.percent:
        highlight_chars = print_needed_chars(args.textfile, args.percent, textchars, vocab)
        if args.highlight:
            (_, progress) = str_progress(vocab.chars, 2000, True, highlight=highlight_chars)
            print(progress)

    # If we're supposed to sort by Jun Da's rank and exclude n=1
    elif args.sort:
        print_sorted_chars(textchars, vocab, args.sort)

    # Otherwise we just want a list of known/unknown characters in the text
    else:
        print_unknown_chars(textchars, vocab)
