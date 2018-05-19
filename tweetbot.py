import tweepy
import json

from secrets import *

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.id_str)
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
    
def get_tweets_by_user(user, api):
    print "Getting tweets by user"
    tweets = api.user_timeline(screen_name=user)
    print "Tweets:", tweets

if __name__ == "__main__":
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)
    
    # read_tweets("eprint.iacr.org", api)
    get_tweets_by_user("fireflixdragoon", api)
    
    
