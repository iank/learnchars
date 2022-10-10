from learnchars.hsk import HSK


def test_hsk():
    """
    This tests HSK lookup class
    """
    hsk = HSK()

    assert hsk.hsk_level('爱') == 1
    assert hsk.hsk_level('孩子') == 2
    assert hsk.hsk_level('会议') == 3
    assert hsk.hsk_level('差不多') == 4
    assert hsk.hsk_level('合同') == 5
    assert hsk.hsk_level('寒暄') == 6
    assert hsk.hsk_level('电路板') is None
