import API
from datetime import datetime
import tweepy

client = API.client

now = datetime.now()

print(now)

#user = client.get_user(username="yolosoloyolo1", user_auth=True)
#userid = user.data.id
#mentions = client.get_users_mentions(userid, user_auth=True)
#for mention in mentions.data: 
    #print(mention.id)

mention_id = []
mention_txt = []
tweets = client.get_users_mentions(id='3388138689', user_auth=True)
print(tweets)
for tweet in tweets.data: 
    mention_txt.append(tweet.text)
for tweet in tweets.data:
    mention_id.append(tweet.id)


#tweet = client.get_tweet(id='1538788393714335745', user_auth=True)
#print(tweet)