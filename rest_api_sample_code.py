import tweepy 
from tweepy import OAuthHandler
import time

consumer_key = 'PrPvdoRpCMFK0PDNdrbwOknY7'
consumer_secret = '6XbyxF2pu2NBi3ih0JaofHFWppPDDm5QZCRMvkTrP1KsaItqQG'
access_token = '114046849-aZ35DKUy7FA2IdntWG8O4Ta52k5e79acbrlUgWpK'
access_secret = 'tNzYowo4e4ZiI1OqcnnYNajvYBlr2HbnLX1RwbYuWWLL8'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

ids_followers = []

for page in tweepy.Cursor(api.followers_ids, str_id="2652300883").pages():
    ids_followers.extend(page)
    time.sleep(1)
    
ids_following = []
    
for page in tweepy.Cursor(api.friends_ids, str_id="2652300883").pages():
      ids_following.extend(page)
      time.sleep(1)

