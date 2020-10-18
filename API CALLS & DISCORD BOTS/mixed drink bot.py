
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
    

    if message.content.startswith("(debug 124)"):
        x = message.content.replace("(debug 124)","")
        await client.change_presence(status=discord.Status.online, activity=discord.Game(x))
    
    
    elif message.content == "<@630330114605056011>":
        name = "**{}**".format(message.mentions[0].name)
        command1 = "**~Jesus**"
        Helpmessage = """
        **Thanks for adding me to {}**!
        
        ***Description***
        Hello my child, I shall share images of myself with you if you call upon me using my command.
        
        ***Commands***
        {}
        
        ***Support The Creator***
                Please support the creator by sharing me to other servers using the following link: 
https://discordapp.com/api/oauth2/authorize?client_id=630330114605056011&permissions=0&scope=bot
        or through the following links.
        -<:patreon:630306170791395348> https://www.patreon.com/b9king
        -<:paypal:630306883105849354> https://www.paypal.com/paypalme2/b9king
        Or you can visit him here: https://benignking.xyz :heart:
        """.format(message.guild.name,command1)
        
        embed=discord.Embed(title="", url="https://www.patreon.com/b9king", description= Helpmessage, color=0x00ffff)
        embed.set_thumbnail(url= message.mentions[0].avatar_url)
        await message.channel.send(embed=embed)   
        
    
    
    if message.content.startswith("~Drink"):
        message.content = message.content.replace("~Drink ","")
        
        try:
            x = ingredientSearch(message.content)
        
        
            embed=discord.Embed(title= x["ingredients"] , color=0x746A69, description = x["recipe"])
            embed.set_author(name= x["name"])
            embed.set_thumbnail(url=x["image"])
            embed.set_footer(text="DO NOT DRINK UNDER AGED, ALWAYS DRINK RESPONSIBLY, IF YOU FEEL YOUR DRINKING MAYBE AN ISSUE PLEASE REACH OUT TO SOMEONE")
            await message.channel.send(embed=embed)        
        except:
            await message.channel.send("COULDN'T FIND THAT INGREDIENT")
client.run('NjM1NDEwNjM5MTcwMzA2MDU4.Xawq0w.HxxzHZ3loiwXNz6dQYkpYxfZXEQ')