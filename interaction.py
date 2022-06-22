from tweetinfo import TweetInfo
from userinfo import UserInfo
import API

class Interaction(): 
    def __init__(self, tweetID) -> None:
        self.tweetID = tweetID
        self.client = API.client
    

    def like_tweet(self): 
        self.client.like(self.tweetID, user_auth=True)

    
    def retweet(self): 
        self.client.retweet(self.tweetID, user_auth=True)

    def make_tweet(self, tweetItem):
        self.client.create_tweet(text=tweetItem, user_auth=True)

    
    def reply_to_tweet(self, tweetItem, tweetID): 
        self.client.create_tweet(in_reply_to_tweet_id=tweetID, text=tweetItem, user_auth=True)