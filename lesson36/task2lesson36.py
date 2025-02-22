#task2lesson36.py


"""
Requests using asyncio and aiohttp

Download all comments from a subreddit of your choice using 
URL: https://api.pushshift.io/reddit/comment/search/ . 

As a result, store all comments in chronological order in JSON and dump them to a file. 
For this task use asyncio and aiohttp libraries for making requests to Reddit API.
"""


import aiohttp
import asyncio
import json
from datetime import datetime

# Pushshift API URL for fetching comments
PUSHSHIFT_URL = "https://api.pushshift.io/reddit/comment/search/"

API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiUHVzaHNoaWZ0LVN1cHBvcnQiLCJleHBpcmVzIjoxNjg1MTA4Nzg4LjE5NzY3OTh9.hATtBHzQh5hiFBSFg3gQsFK2xrwIlPynYrL7l6pPCMw"

# Subreddit to fetch comments from
SUBREDDIT = "python"  # Replace with your desired subreddit

# File to store the comments
OUTPUT_FILE = "comments.json"

async def fetch_comments(session, url, params, headers):
    """Fetch comments from the Pushshift API."""
    async with session.get(url, params=params, headers=headers) as response:
        if response.status == 200:
            data = await response.json()
            return data.get("data", [])
        else:
            print(f"Failed to fetch data: {response.status}")
            return []

async def fetch_all_comments(subreddit, output_file):
    """Fetch all comments from a subreddit and save them in chronological order."""
    comments = []
    params = {
        "subreddit": subreddit,
        "size": 500,  # Number of comments per request (max 500)
        "sort": "asc",  # Sort by chronological order
        "sort_type": "created_utc",  # Sort by creation time
    }
    headers = {
    "Accept": "application/json",  
    "Authorization": f"Bearer {API_TOKEN}"  
    }

    async with aiohttp.ClientSession() as session:
        while True:
            data = await fetch_comments(session, PUSHSHIFT_URL, params, headers)
            if not data:
                break  # No more comments to fetch

            comments.extend(data)
            # Update the 'before' parameter to fetch the next batch of comments
            params["before"] = data[-1]["created_utc"]

    # Sort comments by creation time (ascending order)
    comments.sort(key=lambda x: x["created_utc"])

    # Save comments to a JSON file
    with open(output_file, "w") as f:
        json.dump(comments, f, indent=4)

    print(f"Saved {len(comments)} comments to {output_file}")


if __name__ == "__main__":
    start_time = datetime.now()
    asyncio.run(fetch_all_comments(SUBREDDIT, OUTPUT_FILE))
    end_time = datetime.now()
    print(f"Execution Time: {end_time - start_time}")
