from pkg_resources import resource_filename

HSK_LIST_FILENAME = resource_filename("learnchars", "data/hsk.tsv")


class HSK:
    def __init__(self):
        self._list = {}
        self._load_from_tsv(HSK_LIST_FILENAME)

    def _load_from_tsv(self, filename):
        with open(filename) as f:
            for line in f:
                # Skip comments
                if line[0] == '#':
                    continue

                (level, _, word) = line.split("\t")[0:3]
                self._list[word] = int(level)

    def hsk_level(self, word):
        """Returns the HSK (pre-2021) level of the given word, or None"""
        if word in self._list.keys():
            return self._list[word]
        else:
            return None
