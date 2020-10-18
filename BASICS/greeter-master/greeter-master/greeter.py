
import discord
import asyncio
from discord.utils import find

client=discord.Client()

@client.event
async def on_guild_join(guild):
    allowedID = [536447514447183892]
    if guild.id not in allowedID:
        await guild.leave()

@client.event
async def on_message_delete(message):
    time_str = message.created_at.strftime('%m-%d-%Y %I:%M%p')
    await (await client.fetch_channel(640632330846863426)).send(
        content='{}   {} ({}): {}'.format(time_str, message.author.display_name, message.author.id, message.content)
    )


@client.event
async def on_member_join(member):
    guild = member.guild
    greeting = """Please welcome {0.mention} to {1.name}!
I've DM'd you the help commands for the bots on server. Please introduce yourself and make yourself at home.
""".format(member,guild)
    dm = """Hey, thanks for joining up on the server!
    *Bots*
    If you need any help with the bots feel free to @ mention them and you'll get their help message. If you want to add any of them to a server then that link will be included with it. 
    
    *Roles*
    You'll start off as a new friend on the server, this just means you are new here. You are alaways welcome to come play with us, talk with us, or just join up for whatever. When you're here you should feel like a friend and feel welcome*. You'll recieve old friend once you're a known face around the discord.
    If you feel uncomfortable or are being harassed by another memeber please reach out to one of the admins or myself immediately. 
    
    *If you are wearing out your welcome you will be treated as such
    
    *Important*
    If you joined from Magic The Gathering and would like to be notified when we are playing so you can join up please type "~MTG PLAYER" into any channel in the server. This will give you the role so you can be notified when we play.
    
    If you play TTRPGs like D&D or Call of Cthulhu and would like to join or campaign or find players for your campaign(s), please post in the general and ask for the role.
    
    *Link to the Server*
    https://discord.gg/XSguZkH
    
    
    ***Support The Creator***
    Please support the creator by sharing me to other servers or through the following links.
    -<:patreon:630306170791395348> https://www.patreon.com/b9king
    -<:paypal:630306883105849354> https://www.paypal.com/paypalme2/b9king
    Or you can visit him here: https://benignking.xyz :heart:
"""
    
    x = guild.channels
    y = False
    
    for i in x:
        if i.permissions_for(guild.me).send_messages and not y:
            x = i
            break
    
    rolez = ""
    
    for i in guild.roles:
        if i.name == "New Friends":
            rolez = i
            break
    
    await member.send(dm)
    await x.send(greeting) 
    await member.add_roles(rolez)
    
async def on_message(message):
    
  
    if message.content == ("~MTG PLAYER"):
        print("starting")
        rolez = ""
        for i in message.guild.roles:
            if i.name == "Magic The Gathering Player":
                rolez = i
                break    
        print("rolez")
        await member.add_roles(rolez)

        

                
client.run('NTkxOTI4Nzg4MTYyNTc2NDE2.XQ39SA.Tm9A3cQ_mG0qCERGM6qRBtS6y1I') 

