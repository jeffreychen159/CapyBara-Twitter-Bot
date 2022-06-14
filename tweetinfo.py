import API

class TweetInfo(): 
    def __init__(self, tweetID) -> None:
        self.tweetID = tweetID
        self.client = API.client

    def get_retweeters(self): 
        return self.client.get_retweeters(self.tweetID)

    def get_likers(self): 
        return self.client.get_liking_users(self.tweetID)

    def get_quote_tweeters(self): 
        return self.client.get_quote_tweets(self.tweetID)