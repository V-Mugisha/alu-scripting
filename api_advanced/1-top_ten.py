#!/usr/bin/python3
"""
1-top_ten
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None: Prints titles or None if invalid.
    """
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