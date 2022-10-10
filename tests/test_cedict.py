from learnchars.cedict import CEDICT


def test_cedict():
    """
    This tests the CEDICT lookup class
    """
    cedict = CEDICT()

    assert cedict.lookup('电路板') is None

    entry = cedict.lookup('电脑')
    assert entry.pinyin == 'dian4 nao3'
    assert entry.meanings[0] == 'computer'
