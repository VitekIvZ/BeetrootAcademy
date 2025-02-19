#task1lesson33.py


"""
    Robots.txt

Download and save to file robots.txt from wikipedia, twitter websites etc. 
"""

import requests

# List of websites to download robots.txt from
websites = [
    "https://www.wikipedia.org/robots.txt",
    "https://www.twitter.com/robots.txt",
    # Add more websites as needed
]

# Function to download and save robots.txt
def download_robots_txt(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Extract the domain name for the filename
        domain = url.split("//")[1].split("/")[0]
        filename = f"{domain}_robots.txt"

        # Save the content to a file
        with open(filename, "w") as file:
            file.write(response.text)
        print(f"Downloaded and saved {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")

if __name__ == "__main__":
    
    # Download robots.txt for each website
    for site in websites:
        download_robots_txt(site)
