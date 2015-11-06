#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re
import operator
import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import bigrams


emoticons_str = r"""
	(?:
		[:=;] # Eyes
		[oO\-]? # Nose
		[D\)\]\(]/\\OpP] # Mouth
	)"""

regex_str = [
	emoticons_str,
	r'<[^>]+>', # HTML tags
	r'(?:@[\w_]+)', # @-mentions
	r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hashtags
	r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
	r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
	r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
	r'(?:[\w_]+)', # other words
	r'(?:\S)' # anything else
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE | re.UNICODE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']

def tokenize(s):
	return tokens_re.findall(s)

def preprocess(s, lowercase=False):
	tokens = tokenize(s)
	if lowercase:
		tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
	return tokens

dataset_file = 'tweets_dataset/tweets.json'
with open(dataset_file, "r") as f:
	count_all = Counter()
	count_stop = Counter()
	count_hashtags = Counter()

	for line in f:
		tweet = json.loads(line.strip())
		if 'text' in tweet:
			# Create a list of tokens
			tokens = preprocess(tweet['text'])
			# Create a list of terms
			terms_all = [term for term in preprocess(tweet['text'])]
			# Create a list of terms without stopwords
			terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
			# Count terms only once
			terms_single = set(terms_all)
			# Count hashtags only
			terms_hash = [term for term in preprocess(tweet['text']) if term.startswith('#')]
			# Count terms only (no hashtags, no mentions)
			terms_only = [term for term in preprocess(tweet['text']) if term not in stop and not term.startswith(('#', '@'))]

			# Update counter
			count_all.update(terms_all)
			count_stop.update(terms_stop)
			count_hashtags.update(terms_hash)

#print count_all.most_common(5)
print count_stop.most_common(20)
#print count_hashtags.most_common(5)

terms_bigram = list(bigrams(terms_stop))
#print terms_bigram
