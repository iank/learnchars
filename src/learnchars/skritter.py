import re
import argparse
import requests


class Skritter:
    def __init__(self, filename):
        self.words = _words_from_tsv(filename)
        self.chars = _chars_from_words(self.words)


def _chars_from_words(words):
    chars = []
    for word in words:
        chars.extend([*word])

    return set(chars)


def _words_from_tsv(filename):
    lines = []
    with open(filename) as f:
        lines = f.readlines()

    valid_lines = [line for line in lines if re.match(".*\t.*\t.*\t", line)]
    words = [line.split("\t")[0] for line in valid_lines]
    return set(words)


def api_authenticate(username, password):
    """Authenticate with the legacy Skritter API. Only Resource Owner Password
    Credentials Grant is supported"""
    url = 'https://legacy.skritter.com/api/v0/oauth2/token'
    # The web client's credentials
    client = 'c2tyaXR0ZXJ3ZWI6YTI2MGVhNWZkZWQyMzE5YWY4MTYwYmI4ZTQwZTdk'
    params = {
        "client_id": "skritterweb",
        "grant_type": "password",
        "password": password,
        "username": username
    }

    headers = {
        "Authorization": "basic {}".format(client),
        "Origin": "https://skritter.com",
    }

    resp = requests.post(url, headers=headers, data=params)
    resp.raise_for_status()

    return resp.json()


def api_fetch_entities(token, cursor=None):
    url = 'https://api.skritter.com/v3/items'
    params = {
        "lang": "zh",
        "limit": "1000",
    }

    if cursor is not None:
        params["cursor"] = cursor

    headers = {
        "Authorization": "bearer {}".format(token),
        "Origin": "https://skritter.com",
    }

    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()

    return resp.json()


def api_fetch_by_ids(token, ids):
    url = 'https://api.skritter.com/v3/vocabs/fetch-by-ids'
    params = {
        "data": "|".join(ids),
    }

    headers = {
        "Authorization": "bearer {}".format(token),
        "Origin": "https://skritter.com",
    }

    resp = requests.post(url, headers=headers, data=params)
    resp.raise_for_status()

    return resp.json()


def main():
    p = argparse.ArgumentParser(description='Fetch vocab list from skritter')
    p.add_argument('username', type=str, help='Skritter username')
    p.add_argument('password', type=str, help='Skritter password')
    args = p.parse_args()

    session = api_authenticate(args.username, args.password)
    token = session['access_token']

    vocabids = set()

    cursor = None
    while True:
        ret = api_fetch_entities(token, cursor)
        cursor = ret['cursor']

        vids = [x['vocabIds'][0] for x in ret['entities'] if len(x['vocabIds']) == 1]
        vocabids = vocabids.union(vids)

        if cursor is None:
            break

    # Split into groups of 300, fetch-by-ids
    vocabids = list(vocabids)
    N = 300
    idgroups = [vocabids[i:i + N] for i in range(0, len(vocabids), N)]

    vocab = []
    for group in idgroups:
        ret = api_fetch_by_ids(token, group)
        for entity in ret['entities']:
            vocab.append(entity['writing'])

    vocab = set(vocab)
    for word in vocab:
        print("{}\t\t\t".format(word))


if __name__ == '__main__':
    main()
