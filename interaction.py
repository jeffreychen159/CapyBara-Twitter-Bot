from tweetinfo import TweetInfo
from userinfo import User
import API

class Interaction(): 
    def __init__(self, tweetID) -> None:
        self.tweetID = tweetID
        self.client = API.client
    
    # Likes tweet
    def like_tweet(self) -> None: 
        self.client.like(self.tweetID, user_auth=True)

    # Retweets
    def retweet(self) -> None: 
        self.client.retweet(self.tweetID, user_auth=True)