from pkg_resources import resource_filename
from functools import lru_cache

CHAR_FREQ_FILENAME = resource_filename("learnchars", "data/junda.tsv")


@lru_cache(maxsize=None)
def character_list():
    chars = []
    with open(CHAR_FREQ_FILENAME) as f:
        for line in f:
            # Skip comments
            if line[0] == '#':
                continue

            # Extract character
            (rank, char) = line.split("\t")[0:2]
            chars.append((char, int(rank)))

    return chars


def get_next_character(known_characters, n=1):
    if n < 1:
        raise ValueError("n must be >= 1")

    remaining = n
    found = []
    for (char, rank) in character_list():
        # The list is sorted by frequency, so return this character if it is not known
        if char not in known_characters:
            found.append((char, rank))
            remaining = remaining - 1

        if remaining == 0:
            break

    return found


def str_progress(known_characters, n=1000, invert=False, line_width=50):
    progress = ""
    known_count = 0

    if n < 1:
        raise ValueError("n must be >= 1")

    if not invert:
        known_format = '{}'
        unknown_format = '\u3000'
    else:
        known_format = '\u3000'
        unknown_format = '{}'

    progress += '一' * (line_width + 2) + "\n"
    remaining = n
    pos = 0
    for (char, _) in character_list():
        if pos == 0:
            progress += '｜'

        if char in known_characters:
            progress += known_format.format(char)
            known_count = known_count + 1
        else:
            progress += unknown_format.format(char)

        pos = pos + 1
        if pos == line_width:
            progress += "｜\n"
            pos = 0

        remaining = remaining - 1
        if remaining == 0:
            break

    progress += '一' * (line_width + 2)
    return (known_count / n, progress)


def get_character_rank(character):
    for (char, rank) in character_list():
        if char == character:
            return rank

    return None
