import os

import googleapiclient.discovery

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyDwn0s8RzwuIbevZ2OD_E1w2iclJD6rZqI"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.comments().list(
        part="snippet",
        parentId="UgzDE2tasfmrYLyNkGt4AaABAg"
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()
