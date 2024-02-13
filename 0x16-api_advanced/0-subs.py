#!usr/bin/python3

"""Query Reddit API for number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit.
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    try:
        # Send GET request to Reddit API and
        # Ensure a custom User-Agent to prevent errors.
        response = requests.get(url, headers={'User-Agent': 'My User Agent'},
                                allow_redirects=False)
        return response.json().get("data").get("subscribers")
    except Exception:
        return 0
