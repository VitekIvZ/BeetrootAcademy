#task3lesson34.py


"""
Requests using multithreading

Download all comments from a subreddit of your choice using 
URL: https://api.pushshift.io/reddit/comment/search/ . 

As a result, store all comments in chronological order in JSON and dump it to a file. 
For this task use Threads for making requests to reddit API.
"""

import requests
import json
import threading


subreddit = "python"  
url = "https://api.pushshift.io/reddit/comment/search"

API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiUHVzaHNoaWZ0LVN1cHBvcnQiLCJleHBpcmVzIjoxNjg1MTA4Nzg4LjE5NzY3OTh9.hATtBHzQh5hiFBSFg3gQsFK2xrwIlPynYrL7l6pPCMw"

params = {
    "subreddit": subreddit,
    "size": 1000,  
    "sort": "asc",  
    "sort_type": "created_utc"  
}


headers = {
    "Accept": "application/json",  
    "Authorization": f"Bearer {API_TOKEN}"  
}


comments = []
lock = threading.Lock()


def fetch_comments(before=None):
    local_comments = []
    if before:
        params["before"] = before  

    
    response = requests.get(url, params=params, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch data: {response.status_code} - {response.text}")
        return []

    data = response.json().get("data", [])
    if not data:
        return []  # No more comments to fetch

    local_comments.extend(data)
    print(f"Fetched {len(data)} comments.")
    return local_comments


def threaded_fetch(before=None):
    new_comments = fetch_comments(before)
    with lock:
        comments.extend(new_comments)


def main():
    before = None
    threads = []

    while True:
        
        thread = threading.Thread(target=threaded_fetch, args=(before,))
        threads.append(thread)
        thread.start()

        if threads[-1].is_alive():
            thread.join()  

        
        if threads[-1].is_alive():
            before = comments[-1]["created_utc"]  
        else:
            break  

    
    comments.sort(key=lambda x: x['created_utc'])

    
    output_file = f"{subreddit}_comments.json"
    with open(output_file, "w") as file:
        json.dump(comments, file, indent=4)
    print(f"Saved {len(comments)} comments to {output_file}")

if __name__ == "__main__":
    print(f"Fetching comments from r/{subreddit}...")
    main()

