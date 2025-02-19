#task2lesson35.py


"""
Requests using concurrent and multiprocessing libraries

Download all comments from a subreddit of your choice using 
URL: https://api.pushshift.io/reddit/comment/search/ . 

As a result, store all comments in chronological order in JSON and dump it to a file. 
For this task use concurrent and multiprocessing libraries for making requests to Reddit API.
"""


import requests
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
import json


API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiUHVzaHNoaWZ0LVN1cHBvcnQiLCJleHBpcmVzIjoxNjg1MTA4Nzg4LjE5NzY3OTh9.hATtBHzQh5hiFBSFg3gQsFK2xrwIlPynYrL7l6pPCMw"


def fetch_comments(subreddit, before=None, size=100):
    """
    Fetch comments from a subreddit using the Pushshift API.
    :param subreddit: Name of the subreddit.
    :param before: Timestamp to fetch comments before (for pagination).
    :param size: Number of comments to fetch per request.
    :return: List of comments.
    """
    url = "https://api.pushshift.io/reddit/comment/search/"
    params = {
        "subreddit": subreddit,
        "size": size,
        "sort": "desc",  # Sort by newest first
        "before": before,
    }
    headers = {
    "Accept": "application/json",  
    "Authorization": f"Bearer {API_TOKEN}"  
    }
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json().get("data", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching comments: {e}")
        return []
    
    
def fetch_all_comments(subreddit, max_comments=1000):
    """
    Fetch all comments from a subreddit using concurrent requests.
    :param subreddit: Name of the subreddit.
    :param max_comments: Maximum number of comments to fetch.
    :return: List of comments in chronological order.
    """
    comments = []
    before = None  # Start with the most recent comments
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        while len(comments) < max_comments:
            futures.append(executor.submit(fetch_comments, subreddit, before))
            if len(futures) >= 10:  # Limit the number of concurrent requests
                for future in as_completed(futures):
                    new_comments = future.result()
                    if not new_comments:
                        break
                    comments.extend(new_comments)
                    before = new_comments[-1]["created_utc"]  # Update 'before' for pagination
                futures = []
            time.sleep(1)  # Avoid hitting rate limits
    # Sort comments by creation time in ascending order
    comments.sort(key=lambda x: x["created_utc"])
    return comments[:max_comments]


def save_comments_to_json(comments, filename):
    """
    Save comments to a JSON file.
    :param comments: List of comments.
    :param filename: Name of the output file.
    """
    with open(filename, "w") as f:
        json.dump(comments, f, indent=4)
    print(f"Saved {len(comments)} comments to {filename}")
    
    
def main():
    subreddit = "python"  # Choose a subreddit
    max_comments = 1000  # Maximum number of comments to fetch
    output_file = "reddit_comments.json"

    print(f"Fetching comments from r/{subreddit}...")
    comments = fetch_all_comments(subreddit, max_comments)
    print(f"Fetched {len(comments)} comments.")

    save_comments_to_json(comments, output_file)

if __name__ == "__main__":
    main()