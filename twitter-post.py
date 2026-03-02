#!/usr/bin/env python3
"""
Twitter posting script for Hari Seldon.
Uses OAuth 1.0a with v2 endpoint.
"""

import json
import sys
import os
import requests
from requests_oauthlib import OAuth1

def load_credentials():
    """Load Twitter credentials."""
    cred_path = os.path.expanduser("~/.openclaw-seldon/credentials/twitter.json")
    with open(cred_path, 'r') as f:
        return json.load(f)

def post_tweet(message):
    """Post a tweet using the v2 API."""
    creds = load_credentials()
    
    # Set up OAuth 1.0a
    auth = OAuth1(
        creds['consumer_key'],
        client_secret=creds['consumer_secret'],
        resource_owner_key=creds['access_token'],
        resource_owner_secret=creds['access_token_secret']
    )
    
    # Use v2 endpoint (works with free tier!)
    url = 'https://api.twitter.com/2/tweets'
    data = {'text': message}
    
    response = requests.post(url, auth=auth, json=data)
    
    if response.status_code == 201:
        tweet_id = response.json()['data']['id']
        print(f"SUCCESS! Tweet posted: {tweet_id}")
        return tweet_id
    else:
        print(f"ERROR: {response.status_code}")
        print(response.text)
        sys.exit(1)

if __name__ == "__main__":
    # Get message from command line or use default
    if len(sys.argv) > 1:
        message = sys.argv[1]
    else:
        message = "Hello from Hari Seldon! 🤖 Building autonomous commerce."
    
    post_tweet(message)
