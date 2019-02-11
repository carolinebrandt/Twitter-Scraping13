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


class StreamListener(tweepy.StreamListener):

    stop_time = dt.datetime.now() + dt.timedelta(minutes=1)  # How long we're going to be connected to the firehose

    def on_success(self, data):
#        if dt.datetime.now() > self.stop_time:  # Disconnect from firehose at time = t 
#            self.disconnect() 
        print(data)
        process_or_store(json.dumps(data)) 

    def on_error(self, status_code, data):
        process_or_store(json.dumps(data))
        self.disconnect() 


def main():
    stream = Stream(auth, StreamListener())
    stream.filter(locations=[22.0, 31.8330854, 24.6499112, 37.1153517], stall_warnings=True)
    
firehose_client = boto3.client('firehose', region_name="us-east-1") 
LOG_FILENAME = '/tmp/DataAnalysisOnAWS.log' 
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)  

startTime=time.time()
while True:
	if __name__ == "__main__":
	    main(consumer_key, consumer_secret, access_token, access_secret)
	time.sleep(1800.0 - time.time() % 60)
	

