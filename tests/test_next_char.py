import os
import pytest
from learnchars.skritter import import_from_tsv
from learnchars.chars import get_next_character

FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_files',
)

"""
This tests the retrieval of the next most common unknown character from SUBTLEX-CH
"""


@pytest.mark.datafiles(
    os.path.join(FIXTURE_DIR, 'test_nextchar.tsv'),
)
def test_nextchar(datafiles):
    assert (datafiles / 'test_nextchar.tsv').check(file=1)
    chars = import_from_tsv((datafiles / 'test_nextchar.tsv').realpath())
    next_char = get_next_character(chars)

    assert next_char == ('人', 7)
