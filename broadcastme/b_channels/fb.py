import facebook

class Facebook:
    name = "Facebook"

    def __init__(self):
        self.graph = None

    def login(self, creds):
     user_data=creds[uid]["FACEBOOK"]
     access_token = user_data[1]
     self.graph = facebook.GraphAPI(access_token)


    def post(self, message):
        if not self.graph:
            raise AuthError("Facebook not authenticated")
        self.graph.put_wall_post(message)        

    def required_credentials(self):
        return ['user id', 'access token']
