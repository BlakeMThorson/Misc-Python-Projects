
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
    
    if message.content.startswith("(fuckle knuckle)"):
        x = client.guilds
        
        printGuilds = "I AM IN THE FOLLOWING GUILDS; \n "
        
        for i in x:
            printGuilds += " {}, ".format(i.name)
        await message.channel.send(printGuilds)    
    

    if message.content.startswith("(debug 124)"):
        x = message.content.replace("(debug 124)","")
        await client.change_presence(status=discord.Status.online, activity=discord.Game(x))
    
    
    elif message.content == "<@630330114605056011>":
        name = "**{}**".format(message.mentions[0].name)
        command1 = "**~Taco**"
        Helpmessage = """
        **Thanks for adding me to {}**!
        
        ***Description***
        I tell you how to make tacos
        
        ***Commands***
        {}
        
        ***Support The Creator***
                Please support the creator by sharing me to other servers using the following link: 
https://discordapp.com/oauth2/authorize?client_id=635254372774838289&permissions=0&scope=bot
        or through the following links.
        -<:patreon:630306170791395348> https://www.patreon.com/b9king
        -<:paypal:630306883105849354> https://www.paypal.com/paypalme2/b9king
        Or you can visit him here: https://benignking.xyz :heart:
        """.format(message.guild.name,command1)
        
        embed=discord.Embed(title="", url="https://www.patreon.com/b9king", description= Helpmessage, color=0x00ffff)
        embed.set_thumbnail(url= message.mentions[0].avatar_url)
        await message.channel.send(embed=embed)   
        
    
    
    if message.content.startswith("~Taco"):
        x = Taco()
        
        #name
        
        #recipe
        
        
        
        #mixin URL
        #base_layer_url
        #shell_url
        #seasoning_url
        #URL
        
        taco = """
{}       
        """.format(x["recipe"])
        

        embed=discord.Embed(title= "" , color=0x746A69)
        embed.set_author(name= taco)
        embed.set_thumbnail(url=x[1])
        await message.channel.send(embed=embed)        
                                           
             
client.run('NjM1MjU0MzcyNzc0ODM4Mjg5.XauZAA.45wJdrfBji0YKdOxgmIYfOSJUEI')