#task2lesson33.py


"""
Load data

Download all comments from a subreddit of your choice using 
URL: https://api.pushshift.io/reddit/comment/search/ . 

As a result, store all comments in chronological order in JSON and dump it to a file.
"""

import requests
import json
from datetime import datetime

# Define the subreddit and API endpoint
subreddit = "python"  
url = "https://api.pushshift.io/reddit/comment/search?sort=created_utc&order=desc&agg_size=25&shard_size=1.5&limit=10&track_total_hits=false"

# Your API token (if required)
API_TOKEN = "dV754xMdk8bpnkALJ31dHw.bhypOhyIGoe1hrm7SlTfDpDVSZEkRA"

# Parameters for the API request
params = {
    "subreddit": subreddit,
    "size": 1000,  # Number of comments per request (max 1000)
    "sort": "asc",  # Sort comments in ascending order (oldest first)
    "sort_type": "created_utc"  # Sort by creation time
}

# Headers for authorization (if required)
headers = {
    "Accept": "application/json", # Accept JSON response
    "Authorization": f"Bearer {API_TOKEN}"  # Add token to headers
}

# Function to fetch comments from Pushshift API
def fetch_comments():
    comments = []
    before = None  # Used for pagination

    while True:
        if before:
            params["before"] = before  # Fetch comments older than the last fetched comment

        # Make the request with headers (if token is required)
        response = requests.get(url, params=params, headers=headers)
        if response.status_code != 200:
            print(f"Failed to fetch data: {response.status_code} - {response.text}")
            break

        data = response.json().get("data", [])
        if not data:
            break  # No more comments to fetch

        comments.extend(data)
        before = data[-1]["created_utc"]  # Update 'before' for the next request

        print(f"Fetched {len(data)} comments. Total so far: {len(comments)}")

    return comments

# Function to save comments to a JSON file
def save_comments_to_file(comments, filename):
    with open(filename, "w") as file:
        json.dump(comments, file, indent=4)
    print(f"Saved {len(comments)} comments to {filename}")


if __name__ == "__main__":
    print(f"Fetching comments from r/{subreddit}...")
    comments = fetch_comments()
    output_file = f"{subreddit}_comments.json"
    save_comments_to_file(comments, output_file)
