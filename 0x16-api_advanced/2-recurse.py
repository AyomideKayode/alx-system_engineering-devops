#!/usr/bin/python3

"""recursive function module that queries Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.

    Args:
    - subreddit (str): The name of the subreddit.
    - hot_list (list): List to store the titles of hot articles
      (used for recursion).
    - after (str): Identifier for the next page of results
      (used for pagination).

    Returns:
    - list or None: List containing titles of hot articles or None
      if no results are found.
    """

    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    # Ensure a custom User-Agent to prevent errors.
    headers = {'User-Agent': 'My User Agent'}

    params = {'limit': 100, 'after': after} if after else {'limit': 100}

    try:
        # Send GET request to Reddit API with custom User-Agent and
        # pagination parameters
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        data = response.json()  # Parse response as JSON

        # Check if 'data' key exists and 'children' key exists within it
        if 'data' in data and 'children' in data['data']:
            # Extract the posts from the response
            posts = data['data']['children']
            # Extract titles of posts and append to hot_list
            for post in posts:
                hot_list.append(post['data']['title'])

            # Recursively call the function if there are more pages of results
            if data['data']['after']:
                return recurse(subreddit, hot_list,
                               after=data['data']['after'])
            else:
                # Return hot_list if no more pages of results
                return hot_list
        else:
            # Return None if 'data' or 'children' key doesn't exist
            return None
    except requests.RequestException:
        return None  # Return None if there's any exception during the request
