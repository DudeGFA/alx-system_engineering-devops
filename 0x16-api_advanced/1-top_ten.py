#!/usr/bin/python3
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url,
        headers=headers, params = params, allow_redirects = False)
    if response.status_code == 404:
        print("None")
        return
    res = response.json().get("data")
    [print(child.get('data').get('title')) for child in res.get('children')]
