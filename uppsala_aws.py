import tweepy 
from tweepy import Stream
from tweepy import StreamListener 
import datetime as dt
import json
from tweepy import OAuthHandler
import boto3
import codecs
import logging
import time


consumer_key = 'PrPvdoRpCMFK0PDNdrbwOknY7'
consumer_secret = '6XbyxF2pu2NBi3ih0JaofHFWppPDDm5QZCRMvkTrP1KsaItqQG'
access_token = '114046849-aZ35DKUy7FA2IdntWG8O4Ta52k5e79acbrlUgWpK'
access_secret = 'tNzYowo4e4ZiI1OqcnnYNajvYBlr2HbnLX1RwbYuWWLL8'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def process_or_store(tweet):
  try:
  response = firehose_client.put_record(
  DeliveryStreamName='veera-twitter-data-stream', 
  Record={ 
    'Data': json.dumps(tweet, ensure_ascii=False, encoding="utf-8")+'\n' 
    } ) 
  logging.info(response)
  except Exception: 
  logging.exception("Problem pushing to firehose")    


class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                process_or_store(json.dumps(data)) 
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        self.disconnect() 
        return True
 
def main():
    twitter_stream = Stream(auth, MyListener())
    twitter_stream.filter(locations=[22.0, 31.8330854, 24.6499112, 37.1153517], stall_warnings=True)
    
firehose_client = boto3.client('firehose', region_name="us-east-1") 
LOG_FILENAME = '/tmp/DataAnalysisOnAWS.log' 
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)  

startTime=time.time()
while True:
	if __name__ == "__main__":
	    main()
	time.sleep(1800.0 - time.time() % 60)
	


