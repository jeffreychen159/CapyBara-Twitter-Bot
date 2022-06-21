import API

class UserInfo(): 
    def __init__(self, userID) -> None:
        self.userID = userID
        self.client = API.client 


    def get_followers(self): 
        followers = self.client.get_users_followers(self.userID, user_auth=True)
        follower_list = []
        for follower in followers.data: 
            follower_list.append(follower)
        return follower_list


    def get_tweet_mentions_txt(self): 
        mentions = self.client.get_users_mentions(self.userID, user_auth=True)
        mentions_txt = []
        for mention in mentions.data: 
            mentions_txt.append(mention.txt)
        return mentions_txt


    def get_tweet_mentions_id(self):
        mentions = self.client.get_users_mentions(self.userID, user_auth=True)
        mentions_id = []
        for mention in mentions.data: 
            mentions_id.append(mention.id)
        return mentions_id