#usr/bin/python3

import requests
"""queries the Reddit API and returns the number
of subscriber for a given subreddit
"""


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    - If subreddit is invalid, return 0.
    """
    response = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
    )

    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    else:
        return 0