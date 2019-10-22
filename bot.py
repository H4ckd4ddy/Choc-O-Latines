#!/usr/bin/env python3

import json
import tweepy
import os

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(tweet.text)
        
        if 'décrypter' in tweet.text.lower() or 'Décrypter' in tweet.text.lower():
            print('pas celui la !')
        else:
            print(f"{tweet.user.screen_name}:{tweet.text}")
            if (tweet.user.screen_name != "crypteur") and (not tweet.retweeted) and ('RT @' not in tweet.text):
                self.api.update_status(f"@{tweet.user.screen_name} On dit chiffrer, et pas crypter :)", tweet.id)

    def on_error(self, status):
        print("Error detected")

# Authenticate to Twitter

auth = tweepy.OAuthHandler(os.environ['consumer_api'], os.environ['consumer_api_secret'])
auth.set_access_token(os.environ['acces_token'], os.environ['acces_token_secret'])

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["crypter", "cryptez", "crypté", "cryptée", "cryptés", "cryptées", "cryptage"], languages=["fr"])

