import API

class TweetInfo(): 
    def __init__(self, tweetID) -> None:
        self.tweetID = tweetID
        self.client = API.client

    def get_retweeters(self): 
        retweeters = self.client.get_retweeters(self.tweetID, user_auth=True)
        retweeters_id = []
        for retweeter in retweeters.data: 
            retweeters_id.append(retweeter)
        return retweeters_id

    def get_likers(self): 
        likes = self.client.get_liking_users(self.tweetID, user_auth=True)
        likers_id = []
        for likers in likes.data: 
            likers_id.append(likers)
        return likers_id
        

    def get_quote_tweeters(self): 
        quote_tweeters = self.client.get_quote_tweets(self.tweetID, user_auth=True)
        quote_tweeters_ids = []
        for quote_tweeter in quote_tweeters.data: 
            quote_tweeters_ids.append(quote_tweeter)
        return quote_tweeters_ids