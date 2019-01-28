from __future__ import absolute_import, print_function

import sys
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os
from kafka import KafkaProducer
from kafka.errors import KafkaError

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
try:
    consumer_key = os.environ["TWITTER_CONSUMER_KEY"]
    consumer_secret = os.environ["TWITTER_CONSUMER_SECRET"]
    access_token = os.environ["TWITTER_ACCESS_TOKEN"]
    access_token_secret = os.environ["TWITTER_ACCESS_SECRET"]

except KeyError:
    print("Please set the environment variables for twitter credentials")
    sys.exit(1)

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])


# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def on_data(self, data):
        # Asynchronous by default
        future = producer.send('hello-kafka', data)

        # Block for 'synchronous' sends
        try:
            record_metadata = future.get(timeout=10)
        except KafkaError:
            # Decide what to do if produce request failed...
            pass

        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['basketball'])
