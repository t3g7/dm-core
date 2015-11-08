import json
from time import gmtime, strftime,strptime
from time import mktime
from datetime import datetime
from datetime import timedelta

# Recup des tweets en json
tab = []
dates = []
tweet_id = []
with open('datasets/tweets_dataset_20151027.txt',"r") as data_file:   
	for line in data_file: 
		data = json.loads(line)
		data2 = data['entities']['user_mentions']
		for line in data2:
			if data['in_reply_to_status_id'] != None and line['screen_name'] == "Orange_France":
				tweet_id = tweet_id + [data['in_reply_to_status_id']]
				time = strptime(data['created_at'],"%a %b %d %H:%M:%S +0000 %Y")
				dt = datetime.fromtimestamp(mktime(time))
				dates = dates + [dt]
				# tab = tab + [data['created_at']]
# print tweet_id

heure_tweet3 = []
t = []
with open('datasets/tweets_dataset_20151027.txt',"r") as data_file:   
	for line in data_file: 
		data = json.loads(line)
		for i in range(len(dates)):
			if(tweet_id[i] == data['id']):
				heure_tweet = strptime(data['created_at'],"%a %b %d %H:%M:%S +0000 %Y")
				heure_tweet2 = datetime.fromtimestamp(mktime(heure_tweet))
				delt = dates[i] - heure_tweet2
				heure_tweet3 = [delt] + heure_tweet3


delta = sum(heure_tweet3, timedelta()) / len(heure_tweet3)
print str(delta)
