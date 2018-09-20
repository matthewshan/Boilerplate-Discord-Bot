import discord

class Bot(discord.Client):
    def __init__(self):
        discord.Client.__init__(self)

    @staticmethod
    def getToken():
        f = open('token.txt', 'r')
        token = f.read().strip()
        f.close()
        return token

    async def on_ready(self):
        print('Connected as:', self.user)

    async def on_typing(self, channel, user, when):
        print('User: [{}] typing at time: {}:{}:{}'.format(user.display_name, when.hour-4, when.minute, when.second))

    async def on_message(self, message):
        if(message.content.startswith('hello'):
            await self.send_message(message.channel, 'world')


