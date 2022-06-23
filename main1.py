from numpy import empty
import API
import sentiment
import get_reply
import datetime as dt
from facts import Facts
from tweetinfo import TweetInfo
from userinfo import User
from interaction import Interaction

client = API.client

start_date = dt.date.today()
day_delta = dt.timedelta(days=1)
hour_delta = dt.timedelta(hours=1)
end_date = start_date + day_delta
days = 0

def main(): 
    # Initialization
    user1 = client.get_user(username='capybarafunfact', user_auth=True)
    database = Facts('capybara_facts.txt', 'capybara_facts_used.txt')
    user1_id = User(user1.data['id'])
    replied = []

    if True:  
        #database.get_fact_count()
        #fact = database.get_fact()
        #make_tweet(fact)

        replies = user1_id.get_tweet_mentions()
        for reply in replies: 
            if reply not in replied: 
                message = get_reply.auto_reply_message(reply[1])
                reply_to_tweet(message, reply[0])
                replied.append(reply)
            else: 
                pass
        print(replied)



def make_tweet(tweetItem):
    API.client.create_tweet(text=tweetItem, user_auth=True)

    
def reply_to_tweet(tweetItem, tweetID): 
    API.client.create_tweet(in_reply_to_tweet_id=tweetID, text=tweetItem, user_auth=True)


if __name__ == '__main__': 
    main()