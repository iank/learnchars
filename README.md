# Learnchars

This is a tool to help me pick vocabulary words to learn

- Import known words/characters from [Skritter](https://skritter.com) tsv
- Find next most frequent character in [Jun Da's List](https://lingua.mtsu.edu/chinese-computing/statistics/char/list.php?Which=MO)
- Find top N most frequent words with that character in [wordfreq](https://pypi.org/project/wordfreq/)'s corpus. Return words and frequency scores.

# Building

    poetry run pytest
    poetry run flake8
    poetry install

# Usage

    scripts/get_vocab.py /path/to/skritter_export.tsv [n]

# Example

## Get the three next most common unknown-to-me characters, as well as 5 words containing each

    (zhongwen) ~/learnchars$ ./scripts/get_vocab.py ~/skritter-export-all-2022-10-02_08_01.tsv 3
    Next unknown character: 而 (rank: 36)
    Building prefix dict from [...]/wordfreq/data/jieba_zh.txt ...
    Loading model from cache /tmp/jieba.u94264d3ab9629af3bfd4b31c4913a577.cache
    Loading model cost 0.045 seconds.
    Prefix dict has been built successfully.
    #1:     而      (0.00229)
    #2:     而且    (0.000447)
    #3:     然而    (0.000178)
    #4:     而是    (0.000166)
    #5:     从而    (8.91e-05)
    Next unknown character: 之 (rank: 44)
    #1:     之      (0.00126)
    #2:     之后    (0.000427)
    #3:     之间    (0.000302)
    #4:     之前    (0.000282)
    #5:     之一    (0.000214)
    Next unknown character: 部 (rank: 84)
    #1:     部分    (0.000398)
    #2:     部门    (0.000209)
    #3:     全部    (0.000191)
    #4:     内部    (0.000148)
    #5:     部      (0.000145)

## Get a list of sentences comprised entirely of charactres I know, plus a new character ('并')

    (zhongwen) ~/learnchars$ ./scripts/get_sentences.py ~/skritter-export-all-2022-10-04_09_50.tsv ~/sentences.tsv -c '并' |grep '并没'
    我并没有从那本小说里得到多少乐趣。 - wǒ bìng méiyǒu cóng nà běn xiǎoshuō lǐ dédào duōshao lèqù - I didn't get much enjoyment out of that novel.
    “早上好。”我说，但他并没有回答我的问候。 - zǎoshanghǎo wǒ shuō dàn tā bìng méiyǒu huídá wǒ de wènhòu - Good morning,"" I said, but he didn't return the greeting.

# License

MIT License.

Please see [wordfreq](https://github.com/rspeer/wordfreq) for information about licensing and attribution for the data sources distributed with that module.

Character frequency data from https://lingua.mtsu.edu/chinese-computing/statistics/char/list.php?Which=MO
