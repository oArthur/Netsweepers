import tweepy
with open('./src/twitter-tokens.txt', 'r') as tfile:
    access_token = tfile.readline().strip("\n")
    access_token_secret = tfile.readline().strip("\n")
    consumer_key = tfile.readline().strip("\n")
    consumer_secret = tfile.readline().strip("\n")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

public_tweets = api.home_timeline()
