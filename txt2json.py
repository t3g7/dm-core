import json

list_tweets = []
with open("tweets_dataset/tweets.txt","r") as f:
	for line in f:
		tweet = json.loads(line.strip())
		if 'text' in tweet:
			list_tweets.append(tweet)

with open("tweets_test.json","wb") as f:
	json.dump(list_tweets,f)