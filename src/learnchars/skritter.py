import re


def import_from_tsv(filename):
    words = words_from_tsv(filename)
    chars = []
    for word in words:
        chars.extend([*word])

    return set(chars)


def words_from_tsv(filename):
    lines = []
    with open(filename) as f:
        lines = f.readlines()

    valid_lines = [line for line in lines if re.match(".*\t.*\t.*\t", line)]
    return [line.split("\t")[0] for line in valid_lines]
