# test IoT application
# read data from twitter
# and show on scrollbot

import scrollphathd as sphd
import time
import requests
from twython import TwythonStreamer
from auth import (
    twitter_consumer_key,
    twitter_consumer_secret,
    twitter_token,
    twitter_token_secret
)
# as upside down in scrollbot
sphd.rotate(180)

# check it works - light every pixel

for x in range(17):
    for y in range(7):
        sphd.set_pixel(x, y, 0.25)
sphd.show()
time.sleep(0.5)
sphd.clear()
sphd.show()

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            username = data['user']['screen_name']
            tweet = data['text']
            print("@{}: {}".format(username, tweet))
            msg = "@{}: {}".format(username, tweet)
            sphd.write_string(msg)
            sphd.set_brightness(0.25)

            # assume 4 pixels per char then add 17 for width of display
            for x in range(len(msg) * 4 + 17):
                sphd.show()
                sphd.scroll(1)
                time.sleep(0.05)

stream = MyStreamer(
    twitter_consumer_key,
    twitter_consumer_secret,
    twitter_token,
    twitter_token_secret
)
stream.statuses.filter(track='raspberry pi')
