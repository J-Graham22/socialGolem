import tweepy
import time
import webbrowser
import private

def main():
    api = authenticate_with_tweepy()

    while True:
        like_and_retweet(api)
        time.sleep(10)

def authenticate_with_tweepy():
    auth = tweepy.OAuthHandler(private.TWITTER_APP_KEY, private.TWITTER_APP_SECRET, private.CALLBACK_URI)
    redirect_url = auth.get_authorization_url()
    webbrowser.open(redirect_url)

    auth.set_access_token(private.TWITTER_KEY, private.TWITTER_SECRET)
    api = tweepy.API(auth)
    return api

def like_and_retweet(api):
    username_list = private.USERNAME_LIST
    
    for user in username_list:
        for tweet in tweepy.Cursor(api.home_timeline, id=user, include_entities=True).items(5):
            id = tweet.id
            if not tweet.retweeted:
                api.retweet(id)
            if not tweet.favorited:
                api.create_favorite(id)

if __name__ == '__main__':
    main()