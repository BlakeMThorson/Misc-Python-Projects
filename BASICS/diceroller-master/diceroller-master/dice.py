import discord
import random
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
    
    
    elif message.content == "<@590020147260162079>":
        name = "**{}**".format(message.mentions[0].name)
        command1 = "**~Roll (number of dice)D(number of sides)**"
        Helpmessage = """
        **Thanks for adding me to {}**!
        
        ***Description***
        I roll dice for people, I can roll any number of them and any number of sides.
        
        ***Commands***
        {}
        Example : ~Roll 4D20
        
        ***Support The Creator***
        Please support the creator by sharing me to other servers using the following link: 
https://discordapp.com/api/oauth2/authorize?client_id=590020147260162079&permissions=0&scope=bot
        or through the following links
        -<:patreon:630306170791395348> https://www.patreon.com/b9king
        -<:paypal:630306883105849354> https://www.paypal.com/paypalme2/b9king
        Or you can visit him here: https://benignking.xyz :heart:
        """.format(message.guild.name,command1)
        
        embed=discord.Embed(title="", url="https://www.patreon.com/b9king", description= Helpmessage, color=0x00ffff)
        embed.set_thumbnail(url= message.mentions[0].avatar_url)
        await message.channel.send(embed=embed)   
        
        
    
    
    
    if message.content.startswith("~Roll "):
        
        toRoll = message.content[6:]
        
        D = toRoll.index("D")
        
        number = toRoll[:D]
        sides = toRoll[D+1:]
        
        msg = ""
        x = 0
        y = 0

        
        for i in range(int(number)):
            x = random.randint(1,int(sides)+1)
            msg += ":game_die:{} : {}".format(str(i+1),str(x))
            msg += "\n"
            y+=x
        
        msg += "Total : {}".format(str(y))
        
        
        if len(msg) < 700:
            await message.channel.send(msg)
        else:
            await message.channel.send(":scream: please roll less dice, or less sides. We don't want to flood the discord!")
  #_________________________________________________________________
#________________Help Command_____________________________________
    elif message.content.startswith("(debug 124 dice)"):
        x = message.content.replace("(debug 124 dice)","")
        await client.change_presence(status=discord.Status.online, activity=discord.Game(x))
    
    
    elif message.content == "~Help Dice":
        name = "** Fortune Teller**"
        command1 = "**~Roll** (number of dice)**D**(number of sides)"
        command2 = "**~Conditions** (us zipcode)"
        command3 = "**~Forecast** (us zipcode)"
        command4 = "**~Alerts** (us zipcode)"
        
        Helpmessage = """
        **Thanks for adding me to {}**!
        *I am a Bot that is able to a given number of die/dice with a given number of sides*
        
        My commands are:
        {}
        **Click the embed to support my creator**
        """.format(message.guild.name,command1)
        
        embed=discord.Embed(title="Dice Roller Help", url="https://www.patreon.com/b9king", description= Helpmessage, color=0x00ffff)
        embed.set_thumbnail(url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/198/game-die_1f3b2.png")
        await message.channel.send(embed=embed)        




                
                
client.run('NTkwMDIwMTQ3MjYwMTYyMDc5.XQcKSg.52WJ5pBxM4RFIvvV-Wpv2wvdnAs') 

