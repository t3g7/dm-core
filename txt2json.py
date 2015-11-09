import json
import os, sys

list_tweets = []
if len(sys.argv) > 2:
        with open(sys.argv[1],"r") as f:
                for line in f:
                        tweet = json.loads(line.strip())
                        if 'text' in tweet:
                                list_tweets.append(tweet)

        with open(sys.argv[2],"wb") as f:
                json.dump(list_tweets,f)

else:
        print "Wrong number of arguments"
