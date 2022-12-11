#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    if (subreddit is None or not isinstance(subreddit, str)):
        return 0
    r = requests.get(
        ('http://www.reddit.com/r/{}/about.json'.format(subreddit)),
        headers={
            'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)'}).json()
    return r.get('data', {}).get('subscribers', 0)
