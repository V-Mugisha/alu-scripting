#!/usr/bin/python3
"""Script that fetch 10 hot post for a given subreddit."""
import requests


def top_ten(subreddit):
   """Return number of subscribers if @subreddit is valid subreddit.
    if not return 0."""
   
    if not subreddit:
        print(None)
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyRedditBot/0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json()
        posts = data['data']['children'][:10]
        for post in posts:
            print(post['data']['title'])
    except (KeyError, ValueError):
        print(None)