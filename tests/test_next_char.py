import os
import pytest
from learnchars.skritter import Skritter
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
    s = Skritter(datafiles / 'test_nextchar.tsv')
    next_char = get_next_character(s.chars)

    assert next_char == [('人', 7)]


@pytest.mark.datafiles(
    os.path.join(FIXTURE_DIR, 'test_nextchar.tsv'),
)
def test_nextchar_n(datafiles):
    """
    This tests the retrieval of the next N most common characters
    """
    assert (datafiles / 'test_nextchar.tsv').check(file=1)
    s = Skritter(datafiles / 'test_nextchar.tsv')
    next_char = get_next_character(s.chars, n=2)

    assert next_char == [('人', 7), ('我', 9)]


def test_char_rank():
    """
    This tests looking up a character's frequency
    """
    assert get_character_rank('条') == 214
    assert get_character_rank('捲') == float('inf')
