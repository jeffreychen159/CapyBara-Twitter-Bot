import tweepy
import keys

client = tweepy.Client(
    consumer_key = keys.consumer_key,
    consumer_secret=keys.consumer_secret,
    access_token=keys.access_token,
    access_token_secret=keys.access_token_secret
)

client.create_tweet(text="hello")