import API

class User(): 
    '''Creates a user class where the bot can interact with user data'''
    def __init__(self, userID) -> None:
        self.userID = userID
        self.client = API.client 

    # Gets users who follow a specific user
    def get_followers(self) -> list: 
        followers = self.client.get_users_followers(self.userID, user_auth=True)
        follower_list = []
        for follower in followers.data: 
            follower_list.append(follower)
        return follower_list

    # Gets users who mention a specific user
    def get_tweet_mentions(self) -> list: 
        mentions = self.client.get_users_mentions(self.userID, user_auth=True)
        mentions_txt = []
        if mentions.data == None: 
            return []
        else: 
            for mention in mentions.data: 
                mentions_txt.append((mention.id, mention.text))
            return mentions_txt
