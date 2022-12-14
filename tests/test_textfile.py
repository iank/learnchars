import os
import pytest
from learnchars.textfile import Textfile
from learnchars.skritter import Skritter

FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_files',
)


@pytest.mark.datafiles(
    os.path.join(FIXTURE_DIR, 'textfile.txt'),
)
def test_textfile(datafiles):
    """
    This test demonstrates that the module correctly counts character frequency

    The returned dictionary should contain only the expected characters, and with the
    appropriate frequency values. Further, iterating the dictionary should proceed in
    decreasing order by count. Finally, punctuation/whitespace should be excluded.
    """
    expected_chars = {'我': 4, '学': 2, '习': 1, '中': 3, '文': 3, '喜': 2, '欢': 2}

    assert (datafiles / 'textfile.txt').check(file=1)

    textfile = Textfile(datafiles / 'textfile.txt')
    textchars = textfile.analyze_frequency()
    assert textchars.keys() == expected_chars.keys()

    # Ensure they are in order
    current_count = 4
    for char, count in textchars.items():
        assert count == expected_chars[char]
        assert count <= current_count
        current_count = count


@pytest.mark.datafiles(
    os.path.join(FIXTURE_DIR, 'textfile.txt'),
)
def test_count_characters(datafiles):
    """
    This test checks that the module counts characters correctly, ignoring
    punctuation (both ASCII and Chinese) and whitespace.
    """
    expected_count = 17

    assert (datafiles / 'textfile.txt').check(file=1)

    textfile = Textfile(datafiles / 'textfile.txt')
    charcount = textfile.count_characters()
    assert charcount == expected_count


@pytest.mark.datafiles(
    os.path.join(FIXTURE_DIR, 'textfile.txt'),
    os.path.join(FIXTURE_DIR, 'textfile_vocab.tsv'),
)
def test_unknown(datafiles):
    """
    This test demonstrates that the module correctly identifies unknown characters
    """
    expected_chars = {'我': 4, '习': 1, '文': 3}

    assert (datafiles / 'textfile.txt').check(file=1)
    assert (datafiles / 'textfile_vocab.tsv').check(file=1)

    vocab = Skritter(datafiles / 'textfile_vocab.tsv')

    textfile = Textfile(datafiles / 'textfile.txt')
    textchars = textfile.unknown_characters(vocab)

    assert textchars == expected_chars
