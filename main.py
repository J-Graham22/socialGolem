# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tweepy
import time
import webbrowser
import private

auth = tweepy.OAuthHandler(private.TWITTER_APP_KEY, private.TWITTER_APP_SECRET, private.CALLBACK_URI)
redirect_url = auth.get_authorization_url()
webbrowser.open(redirect_url)

user_pin_input = input("What's the pin value?")

auth.set_access_token(private.TWITTER_KEY, private.TWITTER_SECRET)
api = tweepy.API(auth)

# current users to check for in the loop
nc_sam = "IamNCSam"
punx = "gg_punx"

url_list = []
url_list.append(nc_sam)
url_list.append(punx)

def like_and_retweet():
    for user in url_list:
        for tweet in tweepy.Cursor(api.home_timeline, id=user, include_entities=True).items(5):
            id = tweet.id
            if 't.co' in tweet.text:
                if not tweet.retweeted:
                    api.retweet(id)
                if not tweet.favorited:
                    api.create_favorite(id)

while True:
    like_and_retweet()
    time.sleep(10)
