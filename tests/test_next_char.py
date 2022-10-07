import os
import pytest
from learnchars.skritter import import_from_tsv
from learnchars.chars import get_next_character
from learnchars.chars import get_character_rank

FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_files',
)


@pytest.mark.datafiles(
    os.path.join(FIXTURE_DIR, 'test_nextchar.tsv'),
)
def test_nextchar(datafiles):
    """
    This tests the retrieval of the next most common unknown character
    """
    assert (datafiles / 'test_nextchar.tsv').check(file=1)
    chars = import_from_tsv((datafiles / 'test_nextchar.tsv').realpath())
    next_char = get_next_character(chars)

    assert next_char == [('人', 7)]


@pytest.mark.datafiles(
    os.path.join(FIXTURE_DIR, 'test_nextchar.tsv'),
)
def test_nextchar_n(datafiles):
    """
    This tests the retrieval of the next N most common characters
    """
    assert (datafiles / 'test_nextchar.tsv').check(file=1)
    chars = import_from_tsv((datafiles / 'test_nextchar.tsv').realpath())
    next_char = get_next_character(chars, n=2)

    assert next_char == [('人', 7), ('我', 9)]


def test_char_rank():
    """
    This tests looking up a character's frequency
    """
    assert get_character_rank('条') == 214
