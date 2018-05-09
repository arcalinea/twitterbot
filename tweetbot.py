import tweepy
import json

from secrets import *

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

def read_tweets(keyword, api):
    myStreamListener = MyStreamListener()

    for res in api.search(q=keyword):
        print res.text

def filter_tweets(keyword, api):
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
    myStream.filter(track=[keyword])

def post_tweet(tweet, api):
    api.update_status(tweet)

if __name__ == "__main__":
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)
    
    post_tweet("Hello world", api)
    
    
