from b_channels import get_channels

class Poster:
    def __init__(self, data_file):
        self.channels = get_channels()
        self.data_file = data_file
        if data_file:
            self.auth_data = json.load(data_file)


    def get_channels(self):
        return self.channels.keys()

    def req_credentials(self, channel):
        if channel not in self.channels:
            raise BroadcastError("No such channel '{}'".format(channel))
        return self.channels[channel].required_credentials()
        

    def authenticate(self, channel, creds):
        if channel not in self.channels:
            raise BroadcastError("No such channel '{}'".format(channel))
        self.auth_data[channel] = creds
        json.dumps(self.auth_data, self.data_file)
        
    
    def post(self, channels, message):
        for i in channels:
            if i not in self.channels:
                print ("Skipping {} since it's not a valid channel".format(i))
                continue
            else:
                channel = self.channels[i]
                channel_creds = self.auth_data[i]
                channel.login(channel_creds) # TODO handle errors here
                channel.post(message)
                print ("Posted to {}".format(i))
                
            

        
