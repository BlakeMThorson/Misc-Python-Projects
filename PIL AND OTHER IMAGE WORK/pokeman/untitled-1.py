import discord
import asyncio
from pokedex import *
from autocatcher import *

client = discord.Client()

@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')
    
@client.event
async def on_message(message):
    

   
    if "The wild pokÃ©mon is " in message.content:
        message.content = message.content.replace("\\",'')
        print(message.content)
        pokemonName = message.content.replace("The wild pokÃ©mon is ","")[:-1]
        pokemonName = guesserList(pokemonName)
        if len(pokemonName) == 1:
            pokemonName = pokemonName[0]
        try:
            await message.channel.send(pokemonName)
        except:
            pokemonName = guesserList(pokemonName)
            await message.channel.send(pokemonName)
    elif len(message.embeds) > 0:
        if message.embeds[0].title == "‌‌A wild pokémon has аppeаred!": 
        #msg = await message.channel.fetch_message(648029305431130133)
            msg = message   
            x = byColor(msg.embeds[0].image.url)
            await message.channel.send( x )
    
        catchPokemon("p!catch {}".format(x))
            
client.run('NjQ3NTk3MTUyMDM3NzY1MTIw.XdiARg.BmIBg-OlhWjxKA6ZYqUbmBR5CRM')