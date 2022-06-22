import API
import sentiment
from datetime import datetime
from facts import Facts
from tweetinfo import TweetInfo
from userinfo import UserInfo
from interaction import Interaction

client = API.client

now = datetime.now()
user1 = client.get_user(username='capybarafunfact', user_auth=True)
print(now)
database = Facts('capybara_facts.txt', 'capybara_facts_used.txt')
user1_id = UserInfo(user1.data[id])


database.get_fact_count()
#fact = database.get_fact()