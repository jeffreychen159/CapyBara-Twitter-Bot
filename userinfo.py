import API

class UserInfo(): 
    def __init__(self, userID) -> None:
        self.userID = userID
        self.client = API.client

    def get_following_users(self): 
        return self.client.get_users_followers(self.userID)

    def get_tweet_mentions(self): 
        return self.client.get_users_mentions(self.userID)

    