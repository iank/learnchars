import os
import pytest
import collections
from learnchars.skritter import Skritter

FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_files',
)


@pytest.mark.datafiles(
    os.path.join(FIXTURE_DIR, 'skritter_test_newlines.tsv'),
)
def test_import_newlines(datafiles):
    """
    This test demonstrates that the module handles newlines correctly

    Skritter's export format does not escape or quote commas, newlines, etc in the definition
    field. The workaround is to export using TSV and assume that lines containing three tab
    characters are valid.
    """
    expected_chars = ['主', '要', '瘦', '哦', '啊', '电', '脑', '累', '新', '习', '惯']
    expected_words = ['主要', '瘦', '哦', '啊', '电脑', '累', '新', '习惯']

    assert (datafiles / 'skritter_test_newlines.tsv').check(file=1)
    s = Skritter(datafiles / 'skritter_test_newlines.tsv')
    assert collections.Counter(s.chars) == collections.Counter(expected_chars)
    assert collections.Counter(s.words) == collections.Counter(expected_words)


@pytest.mark.datafiles(
    os.path.join(FIXTURE_DIR, 'skritter_test_unique.tsv'),
)
def test_import_unique(datafiles):
    """
    This test demonstrates that the module handles unique characters correctly

    Importing a file containing 第一, 一个, 个, and 一 should count as three characters.
    """
    expected_chars = ['第', '一', '个']
    expected_words = ['第一', '一个', '个', '一']
    assert (datafiles / 'skritter_test_unique.tsv').check(file=1)

    s = Skritter(datafiles / 'skritter_test_unique.tsv')
    assert collections.Counter(s.chars) == collections.Counter(expected_chars)
    assert collections.Counter(s.words) == collections.Counter(expected_words)
