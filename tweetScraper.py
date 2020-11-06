# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 15:34:18 2020
@author: jmhni
"""
import tweepy
import pandas as pd
import datetime
import time

consumer_key = "some_consumer_key"
consumer_secret = "some_consumer_secret"
access_token = "some_access_token"
access_token_secret = "some_access_token_secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

date = datetime.datetime.now()
currentDate = str(date.year) + "-" + str(date.month) + "-" + str(date.day) + "-" + str(date.hour) + "-" + str(date.minute)

text_query = ("(kunstig intelligens) OR (maskinlæring) OR (algoritme*)")

#without retweets - currently disabled
#new_query = text_query + " -filter:retweets"

max_tweets = 280
language = 'da'
sincedate = currentDate

def twitterScrape():

    #for query in text_query:  
    # Creation of query method using parameters
    tweets = tweepy.Cursor(api.search, q = text_query, lang = language, since = sincedate, count = 280, tweet_mode = 'extended').items(max_tweets)
         
    # Pulling information from tweets iterable object
    # Add or remove tweet information you want in the below list comprehension
    tweets_list = [[tweet.full_text, tweet.created_at, tweet.id_str, tweet.user.name, tweet.user.screen_name, tweet.user.id_str, tweet.user.location, tweet.user.url, tweet.user.description, tweet.user.verified, tweet.user.followers_count, tweet.user.friends_count, tweet.user.favourites_count, tweet.user.statuses_count, tweet.user.listed_count, tweet.user.created_at, tweet.user.profile_image_url_https, tweet.user.default_profile, tweet.user.default_profile_image] for tweet in tweets]
    
    # Creation of dataframe from tweets_list
    # Did not include column names to simplify code
    tweets_df = pd.DataFrame(tweets_list)
        
    tweets_df.to_excel("KunstigIntelligens-"+ str(currentDate)+".xlsx", index=False)
    
    print(tweets_list)
    
twitterScrape()
