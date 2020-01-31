#!/usr/bin/env python3

import os
import random
import json
import tweepy

TRIGGERS = ["pain au chocolat", "pains au chocolat"]

RESPONSES = [
    "On dit CHOCOLATINE !!!",
    "Un pain au chocolat, c'est juste un bout de pain avec du chocolat"
]

class stream_listener(tweepy.StreamListener):

    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):

        if tweet.user.screen_name.lower() == "choc-o-latine":
            return

        if not any(trigger in tweet.text.lower() for trigger in TRIGGERS):
            return
        
        print(f"{tweet.user.screen_name}:{tweet.text}")
        
        if tweet.retweeted or 'RT @' in tweet.text:
            print('Je ne vais pas repondre à tout ceux qui retweet...')
            return

        response = RESPONSES[random.randrange(0, len(RESPONSES))]
        self.api.update_status(f"@{tweet.user.screen_name} {response}", tweet.id)

    def on_error(self, status):
        print("Error detected")


# Authenticate to Twitter
auth = tweepy.OAuthHandler(os.environ['CONSUMER_API'], os.environ['CONSUMER_API_SECRET'])
auth.set_access_token(os.environ['ACCES_TOKEN'], os.environ['ACCES_TOKEN_SECRET'])

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


tweets_listener = stream_listener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=TRIGGERS, languages=["fr"])

