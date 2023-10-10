#usr/bin/python3

""" queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    Function that queries the an API
    - If subreddit is invalid, print None.
    """
    res = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={'User-agent': 'Custom'},
        params={"limit": 10},
    )

    if res.status_code == 200:
        for get_data in res.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            print(title)
    else:
        print(None)
