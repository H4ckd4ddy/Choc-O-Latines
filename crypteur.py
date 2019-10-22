#!/usr/bin/env python3

import os
import random
import json
import tweepy

RESPONSES = [
    "On dit chiffrer, et pas crypter :)",
    "Le terme crypter ou cryptage pas reconnu par le dictionnaire de l’Académie française",
    "Crypter voudrais dire chiffrer une donnée sans en connaître la clé ou la méthode et donc sans pouvoir la déchiffrer ensuite"
]

class stream_listener(tweepy.StreamListener):

    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):

        if tweet.user.screen_name != "crypteur":
            return
        
        print(f"{tweet.user.screen_name}:{tweet.text}")
        
        if 'décrypt' in tweet.text.lower() or 'décrypt' in tweet.text.lower():
            print('Decrypter... cela depend du contexte... donc... ca ira pour cette fois')
        
        if tweet.retweeted or 'RT @' not in tweet.text:
            print('Je ne vais pas repondre à tout ceux qui retweet...')

        if 'crypt' in tweet.user.screen_name or 'chiffre' in tweet.user.screen_name:
            print('C\'est peut-etre un collegue de croisade contre le cryptage, je le laisse faire...')

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
stream.filter(track=["crypter", "cryptez", "crypté", "cryptée", "cryptés", "cryptées", "cryptage"], languages=["fr"])

