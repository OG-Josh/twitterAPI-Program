# sentiment.py
# Demonstrates connecting to the twitter API and accessing the twitter stream
# Author: Josh Y
# Email: joyang@chapman.edu
# Course: CPSC 353
# Assignment: PA01 Sentiment Analysis
# Version 1.3
# Date: March 8, 2021

# Program will connect to twitter's API to access twitter's stream
# ---------------------------------------
# Libraries
import twitter
# import json
import sys
import codecs

# ---------------------------------------
# Authentication Sequence

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

print('Establishing Authentication Credentials')

CONSUMER_KEY = 'Insert Key Here'
CONSUMER_SECRET = 'Insert Key Here'
ACCESS_TOKEN = 'Insert Key Here'
ACCESS_TOKEN_SECRET = 'Insert Key Here'

auth = twitter.oauth.OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# ---------------------------------------
# Input Sequence

count = 1000

q = input('Enter a search term: ')
search_results = twitter_api.search.tweets(q=q, count=count)
statuses = search_results['statuses']

q2 = input('Enter second term: ')
search_results2 = twitter_api.search.tweets(q=q2, count=count)
statuses2 = search_results2['statuses']

# ---------------------------------------
# For First Term
# Iterates through 5 more batches of results by following the cursor

for _ in range(5):
    try:
        next_results = search_results['search_metadata']['next_results']
    except KeyError:
        break

    kwargs = dict([kv.split('=') for kv in next_results[1:].split("&")])

    search_results = twitter_api.search.tweets(**kwargs)
    statuses += search_results['statuses']

# ---------------------------------------
# For Second Term
# Iterates through 5 more batches of results by following the cursor

for _ in range(5):
    try:
        next_results2 = search_results2['search_metadata']['next_results']
    except KeyError:
        break

    kwargs2 = dict([kv.split('=') for kv in next_results2[1:].split("&")])

    search_results2 = twitter_api.search.tweets(**kwargs2)
    statuses2 += search_results2['statuses']

# ---------------------------------------
# For term 1
# Show one sample search result by slicing the list...

status_texts = [status['text']
                for status in statuses]

screen_names = [user_mention['screen_name']
                for status in statuses
                for user_mention in status['entities']['user_mentions']]

hashtags = [hashtag['text']
            for status in statuses
            for hashtag in status['entities']['hashtags']]

words = [w
         for t in status_texts
         for w in t.split()]

# ---------------------------------------
# For term 2
# Show one sample search result by slicing the list...

status_texts2 = [status['text']
                 for status in statuses2]

screen_names2 = [user_mention['screen_name']
                 for status in statuses2
                 for user_mention in status['entities']['user_mentions']]

hashtags2 = [hashtag['text']
             for status in statuses2
             for hashtag in status['entities']['hashtags']]

words2 = [w
          for t in status_texts2
          for w in t.split()]

# ---------------------------------------
# Sentiment Report on both search terms

sent_file = open('AFINN-111.txt')
scores = {}

for line in sent_file:
    term, score = line.split("\t")
    scores[term] = int(score)

score = 0
score2 = 0

for word in words:
    uword = word.encode('utf-8')
    if word in scores.keys():
        score = score + scores[word]

for word2 in words2:
    uword = word2.encode('utf-8')
    if word2 in scores.keys():
        score2 = score2 + scores[word2]

print(q + "'s Score: " + str(score) + "\n")
print(q2 + "'s Score: " + str(score2) + "\n")

if(float(score) > float(score2)):
    print(q + " has more positive sentiment . . . \n")
elif(float(score) < float(score2)):
    print(q2 + " has more positive sentiment . . . \n")
else:
    print("Equal or error in sentiment . . . \n")

# ---------------------------------------
