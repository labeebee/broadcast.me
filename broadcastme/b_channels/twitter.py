import tweepy
from tweepy import OAuthHandler

class Twitter:
    name = "Twitter"

    def __init__(self):
        self.twitter = None

    def login(self, creds):
        ckey = creds['ckey']
        csec = creds['csec']
        atoken = creds['atoken']
        asec = creds['asec']

        auth= OAuthHandler(ckey,csec)
        auth.set_access_token(atoken,asec)
        self.twitter = tweepy.API(auth)

    def post(self, message):
        if not self.twitter:
            raise AuthError("Twitter is not authenticated")
        self.twitter.update_status(message)
        

    def required_credentials(self):
        return ['ckey', 'csec', 'atoken', 'asec']

        
