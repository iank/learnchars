from pkg_resources import resource_filename

CHAR_FREQ_FILENAME = resource_filename("learnchars", "data/junda.tsv")


def get_next_character(known_characters):
    with open(CHAR_FREQ_FILENAME) as file:
        for line in file:
            # Skip comments
            if line[0] == '#':
                continue

            # Extract character
            (rank, char) = line.split("\t")[0:2]

            # The list is sorted by frequency, so return this character if it is not known
            if char not in known_characters:
                return (char, int(rank))

    return None
