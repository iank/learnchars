import collections
import zhon.cedict


def analyze_frequency(filename):
    chars = {}
    with open(filename) as f:
        while True:
            c = f.read(1)
            if not c:
                break

            if c not in zhon.cedict.all:
                continue
            if c == '、':  # evidently the enumeration comma is in cedict
                continue

            if c in chars:
                chars[c] = chars[c] + 1
            else:
                chars[c] = 1

    ordered_chars = collections.OrderedDict()
    for char, count in sorted(chars.items(), key=lambda item: item[1], reverse=True):
        ordered_chars[char] = count

    return ordered_chars
