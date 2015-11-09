import json
from time import gmtime, strftime,strptime
from time import mktime
from datetime import datetime
from datetime import timedelta

# Recup des tweets en json
dates = []
tweet_id = []
with open('tweets_dataset/tweets.txt',"r") as data_file:   
	for line in data_file: 
		data = json.loads(line)
		if 'text' in data:
			data2 = data.get('user').get('screen_name')
			if data2 is not None and len(data2) is not 0:
			 	if data.get('in_reply_to_status_id') and data2 == u'Sosh_fr':
			 		tweet_id = tweet_id + [data.get('in_reply_to_status_id')]
			 		time = strptime(data['created_at'],"%a %b %d %H:%M:%S +0000 %Y")
			 		dt = datetime.fromtimestamp(mktime(time))
			 		dates = dates + [dt]

heure_tweet3 = []
t = []
with open('tweets_dataset/tweets.txt',"r") as data_file:   
	for line in data_file: 
		data = json.loads(line)
		for i in range(len(dates)):
			if(tweet_id[i] == data.get('id')):
				heure_tweet = strptime(data['created_at'],"%a %b %d %H:%M:%S +0000 %Y")
				heure_tweet2 = datetime.fromtimestamp(mktime(heure_tweet))
				delt = dates[i] - heure_tweet2
				heure_tweet3 = [delt] + heure_tweet3

if len(heure_tweet3) is not 0 :
	delta = sum(heure_tweet3, timedelta()) / len(heure_tweet3)
	print str(delta)
