import discord
from sys import exit

class Bot(discord.Client):
    def __init__(self):
        discord.Client.__init__(self)

    @staticmethod
    def getToken():
        try:
            f = open('token.txt', 'r')
            token = f.read().strip()
            f.close()
        except IOError:
            print('A file named token.txt could not be found in this directory')
            exit(1)
        return token

    def fixHour(self, hour):
        '''
        the api gets utc time this converts it to est time and changes it from 24 hour time to 12 hour
        '''
        if(hour >= 4):
            hour -= 4
        else:
            hour += 8
        return hour % 12

    async def on_ready(self):
        print('Connected as:', self.user)

    async def on_typing(self, channel, user, when):
        print('User: [{}] typing at time: {}:{}:{}'.format(user.display_name, self.fixHour(when.hour), when.minute, when.second))

    async def on_message(self, message):
        if(message.content.startswith('hello')):
            await self.send_message(message.channel, 'world')


