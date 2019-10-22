#!/usr/bin/env python3

#import os
import json
import tweepy

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")
        if tweet.user.name != "Crypteur":
            self.api.update_status(f"@{tweet.user.screen_name} On dit chiffrer, et pas crypter :)", tweet.id)

    def on_error(self, status):
        print("Error detected")

# Authenticate to Twitter
auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["crypter", "cryptez", "crypté", "cryptée", "cryptés", "cryptées"], languages=["fr"])