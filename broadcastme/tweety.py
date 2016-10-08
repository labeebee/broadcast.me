from tweepy import OAuthHandler
from .common import load_data
import tweepy
import json


def details(id, data_file):
    data=load_data(data_file)
    id_data=data[id]["TWITTER"]
    consumer_key=id_data[0]
    consumer_secret=id_data[1]
    access_token=id_data[2]
    access_secret=id_data[3]
    return(consumer_key,consumer_secret,access_token,access_secret)


def posting (ckey,csec,atoken,asec,msg):
    auth= OAuthHandler(ckey,csec)
    auth.set_access_token(atoken,asec)
    tweepy.API(auth).update_status(msg)
    return True


    
def new_twitter(uid,ck,cs,at,asc, data_file):
    data=load_data(data_file)
    if "TWITTER" not in data[uid]:
        data[uid]["TWITTER"]=[ck,cs,at,asc]
        f=open("db.json","w")
        json.dump(data,f)
        f.close()
        return True
    else:
        return False


    
