#!/usr/bin/env python
"""
Fetch vocab list from skritter
"""
import argparse
import requests


def skritter_api_fetch_entities(token, cursor=None):
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


def skritter_api_fetch_by_ids(token, ids):
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


if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Fetch vocab list from skritter')
    p.add_argument('token', type=str, help='bearer token')
    args = p.parse_args()

    vocabids = set()

    cursor = None
    while True:
        ret = skritter_api_fetch_entities(args.token, cursor)
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
        ret = skritter_api_fetch_by_ids(args.token, group)
        for entity in ret['entities']:
            vocab.append(entity['writing'])

    vocab = set(vocab)
    for word in vocab:
        print("{}\t\t\t".format(word))
