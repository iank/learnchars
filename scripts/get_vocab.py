#!/usr/bin/env python
"""
- Import known words from word list exported from Skritter.
- Get next most common unknown character from Jun Da's list
- Print five most common words containing that character from wordfreq
"""
import sys
import wordfreq
from pathlib import Path
from learnchars.skritter import import_from_tsv
from learnchars.chars import get_next_character

if __name__ == '__main__':
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        sys.exit("Usage: {} filename.tsv [n]".format(sys.argv[0]))

    tsv_file = Path(sys.argv[1])
    chars = import_from_tsv(tsv_file)

    if len(sys.argv) == 3:
        try:
            n = int(sys.argv[2])
        except ValueError as e:
            sys.exit("Second argument must be numeric")
    else:
        n = 1

    if n < 1:
        sys.exit("n must be >= 1")

    next_chars = get_next_character(chars, n)
    for (next_char, rank) in next_chars:
        print("Next unknown character: {} (rank: {})".format(next_char, rank))

        found_words = 0
        for word in wordfreq.iter_wordlist('zh'):
            if next_char in word:
                found_words = found_words + 1
                print("#{}:\t{}\t({})".format(
                    found_words, word, wordfreq.word_frequency(word, "zh"))
                )

            if found_words == 5:
                break
