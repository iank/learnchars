import collections
import zhon.cedict


class Textfile:
    def __init__(self, filename):
        """Count characters in file"""
        self.chars = {}
        with open(filename) as f:
            while True:
                c = f.read(1)
                if not c:
                    break

                if c not in zhon.cedict.all:
                    continue
                if c == '、':  # evidently the enumeration comma is in cedict
                    continue

                if c in self.chars:
                    self.chars[c] = self.chars[c] + 1
                else:
                    self.chars[c] = 1

    def analyze_frequency(self):
        """Return an OrderedDict with an entry for each character in the file"""
        ordered_chars = collections.OrderedDict()
        for char, count in sorted(self.chars.items(), key=lambda item: item[1], reverse=True):
            ordered_chars[char] = count

        return ordered_chars

    def count_characters(self):
        """Return the total number of characters in the file"""
        chars = self.analyze_frequency()
        return sum(chars.values())

    def unknown_characters(self, vocab):
        """Given a Skritter vocab object, return unknown characters.

        @return: An OrderedDict with an entry for each unknown character
        """
        unknown_chars = self.analyze_frequency()
        for char in vocab.chars:
            if char in unknown_chars.keys():
                unknown_chars.pop(char)

        return unknown_chars
