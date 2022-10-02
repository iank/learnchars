from pkg_resources import resource_filename

CHAR_FREQ_FILENAME = resource_filename("learnchars", "data/junda.tsv")


def get_next_character(known_characters, n=1):
    if n < 1:
        raise ValueError("n must be >= 1")

    remaining = n
    found = []
    with open(CHAR_FREQ_FILENAME) as f:
        for line in f:
            # Skip comments
            if line[0] == '#':
                continue

            # Extract character
            (rank, char) = line.split("\t")[0:2]

            # The list is sorted by frequency, so return this character if it is not known
            if char not in known_characters:
                found.append((char, int(rank)))
                remaining = remaining - 1

            if remaining == 0:
                break

    return found
