import json
from time import gmtime, strftime,strptime
from time import mktime
from datetime import datetime
from datetime import timedelta

# Recup des tweets en json
tab = []
with open('datasets/tweets_dataset_20151027.txt',"r") as data_file:   
	for line in data_file: 
		data = json.loads(line)
		tab = tab + [data['created_at']]

# Conversion en datetime
dates = []
with open('datasets/tweets_dataset_20151027.txt',"r") as data_file:   
	for line in data_file:
		data = json.loads(line)
		time = strptime(data['created_at'],"%a %b %d %H:%M:%S +0000 %Y")
		dt = datetime.fromtimestamp(mktime(time))
		dates = dates + [dt]

# Temps moyen entre deux tweets
t = []
for i in range(len(dates)-1):
	m = dates[i+1] - dates[i]
	t = [m] + t
	
delta = sum(t, timedelta()) / len(t)
print str(delta)
