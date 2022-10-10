import re


class Skritter:
    def __init__(self, filename):
        self.words = _words_from_tsv(filename)
        self.chars = _chars_from_words(self.words)


def _chars_from_words(words):
    chars = []
    for word in words:
        chars.extend([*word])

    return set(chars)


def _words_from_tsv(filename):
    lines = []
    with open(filename) as f:
        lines = f.readlines()

    valid_lines = [line for line in lines if re.match(".*\t.*\t.*\t", line)]
    words = [line.split("\t")[0] for line in valid_lines]
    return set(words)
