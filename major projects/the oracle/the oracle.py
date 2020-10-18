import discord
import random
from asd import *
import asyncio
client=discord.Client()

@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

emojis = {
    "How you feel about yourself" : "<:self:745060377825640609>",
    'What you want most right now' : "<:want:745060377745948753>",
    'Your fears' : "<:fear:745060377540165743>",
    'What is going for you' : "<:workFor:745060377544491052>",
    'What is going against you' : "<:workAgainst:745060377699811389>",
    'The Likely Outcome' : "<:outcome:745060377775046716>"
    }


    
@client.event
async def on_message(message):
    if message.content.startswith("~Oracle"):
        
        #stop myself from having to type message constantly
        author = message.author
        
        #the message for the base embed
        toSend = """<:self:745060377825640609> : How you feel about yourself 
        <:want:745060377745948753> : What you want the most 
        <:fear:745060377540165743> : Your Fears 
        <:workFor:745060377544491052> : What is working for you
        <:workAgainst:745060377699811389> : What is working against you
        <:outcome:745060377775046716> : The likely outcome of it all 
        """
        #reactions that will get added 
        reactions = [ "<:self:745060377825640609>", "<:want:745060377745948753>","<:fear:745060377540165743>","<:workFor:745060377544491052>","<:workAgainst:745060377699811389>","<:outcome:745060377775046716>"]
        
        #send the BASE unedited embed
        embed=discord.Embed(title= "Hello {}, Click A Reaction To Have Your Tarot Reading".format(message.author.name.title()) , color=0x000000, description = toSend)
        embed.set_thumbnail(url="https://www.pinclipart.com/picdir/big/499-4996727_cell-phone-video-obtained-by-hawaii-news-now.png")
        embed.set_footer(text="🌎 BenignKing.xyz - Paypal.me/B9king - Patreon.com/B9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")
        await message.channel.send(embed=embed)  
        
        #get the message information to pass it to other functions
        OracleEmbed = await message.channel.history().get(author=client.user)
        OracleID = OracleEmbed.id 
        
        #add the reactions
        for react in reactions:
            await OracleEmbed.add_reaction(react)
        
        #sleep for a little bit
        await asyncio.sleep(10)   
        
        
        #get the updated version of it reactions and all 
        OracleEmbed = msg = await message.channel.fetch_message(OracleID)        
        
        #get the reactions
        userReact = []
        for reaction in OracleEmbed.reactions:
            async for user in reaction.users():
                if user.id == author.id:
                    userReact.append(reaction.emoji)
        
        #print out the reactions to test it
        print(userReact)
        
        #remove the reactions
        for i in range(len(reactions)-1, -1, -1):
            await OracleEmbed.clear_reaction(reactions[i])
            
        #if the user hit more than 1 thing
        if len( userReact ) != 1:
                embed=discord.Embed(title="!$%# YOU MADE ME DROP MY BALL!", description="Hey, {}, choose only one thing next time!".format(author.name.title()), color=0x000000)
                embed.set_thumbnail(url= "https://files.catbox.moe/rdd5gh.png")
                embed.set_footer(text="🌎 BenignKing.xyz - Paypal.me/B9king - Patreon.com/B9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")
                await OracleEmbed.edit(embed=embed) 
        
        #else get the reading
        else:
            
        #turn the card over    
            embed=discord.Embed(title="Follow these instructions", description="In your mind's eye, picture a deck of cards, slowly shuffle them, and pick the one off the top.".format(author.name.title()), color=0x000000)
            embed.set_thumbnail(url= "https://i.pinimg.com/736x/a3/1e/88/a31e8899d92acb64cf3fff5f5acd6523--vintage-playing-cards-trump-card.jpg")
            embed.set_footer(text="🌎 BenignKing.xyz - Paypal.me/B9king - Patreon.com/B9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")
            await OracleEmbed.edit(embed=embed) 
            
            await asyncio.sleep(10)  
            
            
            names = {
        "self" : "How you feel about yourself", 
        "want" : 'What you want most right now',
        "fear" : "Your fears",
        "workFor" : 'What is going for you',
        "workAgainst" : 'What is going against you',
        "outcome" : 'The Likely Outcome' 
        }
            
        reading = getReading( names[userReact[0].name] )
        
        embed=discord.Embed(title=reading[0], description= reading[2], color=0x000000)
        embed.set_thumbnail(url= reading[1])
        embed.set_footer(text="🌎 BenignKing.xyz - Paypal.me/B9king - Patreon.com/B9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")
        await OracleEmbed.edit(embed=embed) 

client.run('NzQ1MDUxMjEwMDI5MjAzNDg2.XzsJAg.07fsEoTpS79PRwv48JBa9DZ3ofE') 

