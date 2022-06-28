from . import fb
from . import twitter

def get_channels():
    t = twitter.Twitter()
    f = fb.Facebook()
    
    return {f.name : f,
            t.name : t}
