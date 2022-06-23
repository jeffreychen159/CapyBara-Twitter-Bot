from tweetinfo import TweetInfo
from userinfo import User
import API

class Interaction(): 
    def __init__(self, tweetID) -> None:
        self.tweetID = tweetID
        self.client = API.client
    

    def like_tweet(self): 
        self.client.like(self.tweetID, user_auth=True)

    
    def retweet(self): 
        self.client.retweet(self.tweetID, user_auth=True)