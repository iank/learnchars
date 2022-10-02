# Learnchars

This is a tool to help me pick vocabulary words to learn

- Import known words/characters from [Skritter](https://skritter.com) tsv
- Find next most frequent character in [SUBTLEX-CH](https://chrplr.github.io/openlexicon/datasets-info/SUBTLEX-CH/README-subtlex-ch.html)
- Find top N most frequent words with that character in SUBTLEX-CH. Return words and frequency scores.

# Building

poetry run pytest
poetry run flake8
poetry install
