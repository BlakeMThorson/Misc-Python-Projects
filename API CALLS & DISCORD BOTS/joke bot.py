
import discord
import random
from asd import *
client=discord.Client()

@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')
    
@client.event
async def on_message(message):
    if message.content.startswith("~Joke"):
        embed=discord.Embed(title= jokeApiCategory() , color=0xffffff)
        embed.set_author(name="HAHA FUNNY JOKE:")
        embed.set_thumbnail(url="https://logodix.com/logo/751407.png")
        await message.channel.send(embed=embed)        
        

client.run('NjI4MDY4ODI0OTM5MjMzMzAz.XZF03A.unMcKGje3I5Cj3ddoMzwzArUEKw') 

