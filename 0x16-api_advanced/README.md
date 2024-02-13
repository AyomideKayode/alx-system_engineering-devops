# Project: 0x16. API advanced

![api_guide](./api_guide.png)

## Background Context

Questions involving APIs are common for interviews. Sometimes they’re as simple as ‘write a Python script that queries a given endpoint’, sometimes they require you to use recursive functions and format/sort the results.

A great API to use for some practice is the Reddit API. There’s a lot of endpoints available, many that don’t require any form of authentication, and there’s tons of information to be parsed out and presented. Getting comfortable with API calls now can save you some face during technical interviews and even outside of the job market, you might find personal use cases to make your life a little bit easier.

## Resources

### Read or watch:-

- [Reddit API Documentation](https://www.reddit.com/dev/api/)
- [Query String](https://en.wikipedia.org/wiki/Query_string)

## Learning Objectives

### General

- How to read API documentation to find the endpoints you’re looking for
- How to use an API with pagination
- How to parse JSON results from an API
- How to make a recursive API call
- How to sort a dictionary by value

## Tasks

0. [How many subs?](./0-subs.py) :

Write a function that queries the [Reddit API](https://www.reddit.com/dev/api/) and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.

Hint: No authentication is necessary for most features of the Reddit API. If you’re getting errors related to Too Many Requests, ensure you’re setting a custom User-Agent.

Requirements:

- Prototype: def number_of_subscribers(subreddit)
- If not a valid subreddit, return 0.
- NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

First code submission for Task 0

```py
def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit.
    Args:     - subreddit (str): The name of the subreddit.
    Returns:  - int: Number of subscribers, or 0 if the subreddit is invalid.
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    try:
        # Send GET request to Reddit API
        # Ensure a custom User-Agent to prevent errors.
        response = requests.get(url, headers={'User-Agent': 'My User Agent'},
                                allow_redirects=False)
        data = response.json()  # Parse response as JSON

        # Check if 'data' key exists and 'subscribers' key exists within it
        if 'data' in data and 'subscribers' in data['data']:
            # Return the number of subscribers
            return data['data']['subscribers']
        else:
            # Return 0 if 'data' or 'subscribers' key doesn't exist
            return 0
    except Exception:
        # Return 0 if there's any exception during the request
        return 0
```

| Task           | File                           |
| -------------- | ------------------------------ |
|                |
| 1. Top Ten     | [1-top_ten.py](./1-top_ten.py) |
| 2. Recurse it! | [2-recurse.py](./2-recurse.py) |
