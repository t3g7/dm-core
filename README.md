# Test scripts for data mining Twitter

## Setup the app

Go to https://apps.twitter.com to create a new app and get OAuth keys and tokens, then fill ```twitter_oauth.json``` in with these.
Now download necessary dependencies with ```pip install -r requirements.txt```

## Fetch tweets

Run ```python get_tweets.py``` for fetching tweets with either the Search or the Streaming API.

## Produce JSON file

Run ```python txt2json.py``` to produce a valid JSON file.

## And analyze them

The script ```analyze_tweets.py``` uses the precedent JSON file and prints recurrent words, hashtags, etc.
