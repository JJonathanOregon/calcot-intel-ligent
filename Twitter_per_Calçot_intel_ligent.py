#!/usr/bin/env python

import tweepy

auth = tweepy.OAuthHandler('API-KEY-HERE', 'API-PASSWORD-KEY-HERE')
auth.set_access_token('TOKEN-KEY-HERE', 'TOKEN-PASSWORD-KEY-HERE')
api = tweepy.API(auth)

message = input("Tuit: ")
api.update_status(status=message, place_id='Calçot Capital')
