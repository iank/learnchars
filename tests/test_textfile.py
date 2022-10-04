import os
import pytest
from learnchars.textfile import analyze_frequency

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
    expected_chars = {'我': 3, '学': 2, '习': 1, '中': 3, '文': 3, '喜': 2, '欢': 2}

    assert (datafiles / 'textfile.txt').check(file=1)
    textchars = analyze_frequency((datafiles / 'textfile.txt'))
    assert textchars.keys() == expected_chars.keys()

    current_count = 3
    for char, count in textchars.items():
        print(char)
        assert count == expected_chars[char]
        assert count <= current_count
        current_count = count
