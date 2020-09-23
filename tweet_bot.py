from apscheduler.schedulers.blocking import BlockingScheduler
from random import choice
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

sched = BlockingScheduler()
                    
@sched.scheduled_job('interval', hours=3)
def timed_job():
    s=open("sentences.txt","r",encoding="utf-8")
    m=s.readlines()
    l=[]
    for i in range(0,len(m)-1):
        x=m[i]
        z=len(x)
        a=x[:z-1]
        l.append(a)
    l.append(m[i+1])
    o=choice(l)
    api.update_status(o)
    s.close()

@sched.scheduled_job('interval', hours=6)
def timed_job2():
    s=open("samples.txt","r",encoding="utf-8")
    m=s.readlines()
    l=[]
    for i in range(0,len(m)-1):
        x=m[i]
        z=len(x)
        a=x[:z-1]
        l.append(a)
    l.append(m[i+1])
    o=choice(l)
    api.update_status(o)
    s.close()

sched.start()