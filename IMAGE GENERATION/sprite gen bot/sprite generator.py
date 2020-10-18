import discord
from os import system
users = {}

client=discord.Client()

@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')


    
@client.event
async def on_message(message):
    if message.content.startswith("~Sprite"):
        system('something.py 7 1 1900')
        await message.channel.send(file=discord.File('Sprite.jpg'))

                
client.run('NTg5OTUwNzc4MjAzMTc2OTYx.XQbIqA.wDIC9hziuB5Z34iSl67gonIdNdw') 