#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, print None.
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )

    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            print(title)
    else:
        print(None)

# #usr/bin/python3

# """ queries the Reddit API and prints the titles
# of the first 10 hot posts listed for a given subreddit
# """

# import requests


# def top_ten(subreddit):
#     """
#     Function that queries the an API
#     - If subreddit is invalid, print None.
#     """
#     response = requests.get(
#         "https://www.reddit.com/r/{}/hot.json".format(subreddit),
#         headers={'User-agent': 'Google Chrome Version 81.0.4044.129'},
#         params={"limit": 10},
#     )

#     if response.status_code == 200:
#         for get_data in response.json().get("data").get("children"):
#             dat = get_data.get("data")
#             title = dat.get("title")
#             print(title)
#     else:
#         print(None)
