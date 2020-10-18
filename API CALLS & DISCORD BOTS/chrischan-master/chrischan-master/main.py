
import discord
import helper
from helper import *
client=discord.Client()

@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')



@client.event
async def on_guild_join(guild):
    
    name = "**<:Png:590089990780878848> Christian Weston Chandler Bot**"

    
    join_message = """Hello {}
    I'm {}, created by b9king#6857 with help from I am Moonslice#4132
    My commands are:
    {}
    {}
    {}
    {}
    {}
    {}
    {}
    You can support my creator here: https://www.patreon.com/b9king
    """.format(guild.name,name,command1,command2,command3,command4,command5,command6,command7)    
    
    x = guild.channels
    y = False
    
    for i in x:
        if i.permissions_for(guild.me).send_messages and not y:
            x = i
            break
    await x.send(join_message)
            
    
    
    #general.permissions_for(guild.me).send_messages:
        #await general.send(join_message)
    
@client.event
async def on_message(message):
    
 
  
    if message.content.startswith("(debug 124)"):
        x = message.content.replace("(debug 124)","")
        await client.change_presence(status=discord.Status.online, activity=discord.Game(x))
    
    
    elif message.content == "<@590092097609138196>":
        name = "**{}**".format(message.mentions[0].name)
        command1 = "~Qotn Get the *Quote Of The Now*"
        command2 = "~Begging Get Chris' begging stats"
        command3 = "~Tdic Get the *This Day In Christory*"
        command4 = "~Dyk Get the *Did You Know* about Chris"
        command5 = "~Aotn Get the *Article of the Now*"
        command6 = "~Cwcki (name) will try to summarize an article for you and link you it"
        command7 = "~Christorian gives you the link to dive into the rabbit hole!"
        Helpmessage = """
        **Thanks for adding me to {}**!
        
        ***Description***
        I am the CWCki bot. I give out information about the mayor of CWCville, the beloved, Christian Weston Chandler. Please don't bully/ troll them, they need help more than anything at this point.
        
        ***Commands***
        {}
        {}
        {}
        {}
        {}
        {}
        {}
        
        ***Support The Creator***
        Please support the creator by sharing me to other servers using the following link: 
https://discordapp.com/api/oauth2/authorize?client_id=590092097609138196&permissions=0&scope=bot
        or through the following links.
        -<:patreon:630306170791395348> https://www.patreon.com/b9king
        -<:paypal:630306883105849354> https://www.paypal.com/paypalme2/b9king
        Or you can visit him here: https://benignking.xyz :heart:
        """.format(message.guild.name,command1,command2,command3,command4,command5,command6,command7)
        
        embed=discord.Embed(title="", url="https://www.patreon.com/b9king", description= Helpmessage, color=0x00ffff)
        embed.set_thumbnail(url= message.mentions[0].avatar_url)
        await message.channel.send(embed=embed)   
        
        
    
    
    if message.content == "~Qotn":
        x = quoteOfTheNow()
        embed=discord.Embed(title="", color=0x4eda12)
        #embed.set_author(name="Quote Of The Now:", icon_url="https://files.catbox.moe/29zpbx.PNG")
        embed.add_field(name="Quote Of THe Now:", value= x, inline=True)
        await message.channel.send(embed=embed)    

    elif message.content == "~Begging":
        x = chrisChanBegging()
        
        z = ""
        
        for i in x:
            z += i + "\n"
        
        embed=discord.Embed(title="", color=0x4eda12)
        embed.add_field(name="Financhu:", value= z, inline=True)
        await message.channel.send(embed=embed)   

    elif message.content == "~Tdic":
        x = thisDayInChristory()
        embed=discord.Embed(title="", color=0x4eda12)
        embed.add_field(name="This Day In Christory:", value= x, inline=True)
        await message.channel.send(embed=embed)  

    elif message.content == "~Dyk":
        x = didYouKnow()
        z = ""
        for i in x:
            z += "âšªï¸�ï¸�" + i + "\n" 
        embed=discord.Embed(title="", color=0x4eda12)
        embed.add_field(name="Did You Know:", value= z, inline=True)
        await message.channel.send(embed=embed)  
    
    elif message.content == "~Aotn":
        x = articleOfTheNow()
        link = x[1]
        x = x[0]
        embed=discord.Embed(title="Click here for article", color=0x4eda12, url = link)
        embed.add_field(name="Article Of The Now:", value= x, inline=True)
        await message.channel.send(embed=embed)    

    elif message.content.startswith( "~Cwcki"):
        link = ""
        z = message.content.replace("~Cwcki ","")
        x = articleSummary(z)
        embed=discord.Embed(title="", color=0x4eda12, url = link)
        embed.add_field(name= z, value= x[0] + "\n" + x[1], inline=True)
        await message.channel.send(embed=embed)    
        
    elif message.content == "~Christorian":
        x = rabbitHole()
        embed=discord.Embed(title="Become a Christorian", color=0x4eda12, url = x[0])
        await message.channel.send(embed=embed)   
        
 #_________________________________________________________________
#________________Help Command_____________________________________
    elif message.content.startswith("(debug 124 CWC)"):
        x = message.content.replace("(debug 124 CWC)","")
        await client.change_presence(status=discord.Status.online, activity=discord.Game(x))
    
    
    elif message.content == "~Help CWC":
        name = "**ðŸŽ± Fortune Teller**"
        command1 = "~Qotn Get the *Quote Of The Now*"
        command2 = "~Begging Get Chris' begging stats"
        command3 = "~Tdic Get the *This Day In Christory*"
        command4 = "~Dyk Get the *Did You Know* about Chris"
        command5 = "~Aotn Get the *Article of the Now*"
        command6 = "~Cwcki (name) will try to summarize an article for you and link you it"
        command7 = "~Christorian gives you the link to dive into the rabbit hole!"
    
        
        Helpmessage = """
        **Thanks for adding me to {}**!
        *I'm a bot that can give you a rundown on the creator of Sonichu *
        
        My commands are:
        {}
        {}
        {}
        {}
        {}
        {}
        {}
        
        **Click the embed to support my creator**
        """.format(message.guild.name,command1,command2,command3,command4,command5,command6,command7)
        
        embed=discord.Embed(title="CWCki Bot Help", url="https://www.patreon.com/b9king", description= Helpmessage, color=0x00ffff)
        embed.set_thumbnail(url="https://files.catbox.moe/pky9p3.png")
        await message.channel.send(embed=embed)    
    



                
                
client.run('NTkwMDkyMDk3NjA5MTM4MTk2.XQdMMg.0wbU5CA1Xq_KbtYEc0aNnbUAj_0') 

