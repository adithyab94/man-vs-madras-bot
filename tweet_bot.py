from apscheduler.schedulers.blocking import BlockingScheduler
from random import choice
import templates
import word_collections as wc
import tweepy
import os
from os import environ

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def get_story():
    sentence = choice(templates.template)
    sen_lst = sentence.split()
    placeholder = []
    bracket_ph = ["[","]"]
    for wrd in sen_lst:
        if "[" in wrd:
            placeholder.append(wrd)
    for ph in placeholder:
        for bracket in bracket_ph:
            ph=str(ph).replace(bracket,"")
        ph=ph.replace(".","")
        word_lst = wc.collections[ph]
        word = choice(word_lst)
        sentence = sentence.replace(ph,word)
    for bracket in bracket_ph:
        sentence=sentence.replace(bracket,"")
    return(sentence)
    

sched = BlockingScheduler()
                    
@sched.scheduled_job('interval', hours=3)
def timed_job():
    api.update_status(get_story())

sched.start()