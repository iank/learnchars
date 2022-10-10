from pkg_resources import resource_filename
from cedict_utils.cedict import CedictParser

CEDICT_FILENAME = resource_filename("learnchars", "data/cedict_ts.u8")


class CEDICT:
    def __init__(self):
        self._entries = {}
        self._load_cedict(CEDICT_FILENAME)

    def _load_cedict(self, filename):
        parser = CedictParser()
        parser.read_file(filename)
        entries = parser.parse()
        for entry in entries:
            self._entries[entry.simplified] = entry

    def lookup(self, word):
        """Returns the CEDICT entry for the given simplified Chinese word, or None"""
        if word in self._entries.keys():
            return self._entries[word]
        else:
            return None
