from helper import *
import discord
import asyncio
from discord.utils import find

client=discord.Client()

@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')
    
@client.event
async def on_message(message):
    
    check = False
    alert = True
        
    
    if message.content.startswith("~Weather"):
        z = message.content.replace("~Weather ","")
        if z in ["hell","Hell"]:
            embed=discord.Embed(title="Current Weather For Hell:", description="Currently 10,000°F : Feels like **ETERNAL DAMNATION**", color=0x00ffff)
            embed.set_thumbnail(url="https://static.thenounproject.com/png/209550-200.png")
            await message.channel.send(embed=embed)   
            check = True
        elif not z.isdigit() and check == False:
            await message.channel.send("hey this wasn't a zipcode")
        elif z.isdigit() and check == False:
            try:
                x = current(z)
                check = True
            except:
                await message.channel.send("hey that isn't a valid ***US ZIPCODE***")
            if check:
                embed=discord.Embed(title="Current Weather For {}:".format(x[0]), description="Currently {} : {}".format(x[1],x[5]), color=0x00ffff)
                embed.set_thumbnail(url=x[2])
                await message.channel.send(embed=embed)


#____________________________________________________________________________________________________________________________________

    elif message.content.startswith("~Alerts"):
        z = message.content.replace("~Alerts ","")
        
        if not z.isdigit() and check == False:
            await message.channel.send("😢 hey this wasn't a zipcode")
            check = True
        elif z.isdigit() and check == False:
            try:
                x = current(z)
                check = True
                
                if x[3] == "There are currently no weather advisories!":
                    alert = False
                
            except:
                await message.channel.send("😞 hey that isn't a valid ***US ZIPCODE***")
            
            if check and alert:
                embed=discord.Embed(title="Weather Alerts for {}".format(x[0]), url= x[4] , description="{}".format(x[3]), color=0xff0000)
                embed.set_thumbnail(url="https://ui-ex.com/images/increated-clipart-red-alert-3.png")
                await message.channel.send(embed=embed)
            else:
                embed=discord.Embed(title="There are no alerts for {}:".format(x[0]), description="Let's hope it stays that way!", color=0x00ff00)
                embed.set_thumbnail(url="http://chittagongit.com/download/354591")
                await message.channel.send(embed=embed)
                
#_________________________________________________________________________________________________________________________________________________________________________

    elif message.content.startswith("~Forecast"):
        z = message.content.replace("~Forecast ","")
        if not z.isdigit() and check == False:
            await message.channel.send("😢 hey this wasn't a zipcode")
        elif z.isdigit() and check == False:
            try:
                x = current(z)
                check = True
            except:
                await message.channel.send("😞 hey that isn't a valid ***US ZIPCODE***")
            if check:
                throw = ""
                embed=discord.Embed(title="Forecast For {}:".format(x[0]), description="{}".format(x[11]), color=0x00ffff)
                embed.set_thumbnail(url=x[12])
                await message.channel.send(embed=embed)

#________________________________________________________________________________________________________________________________________________________________________



    elif message.content.startswith("~Conditions"):
        z = message.content.replace("~Conditions ","")
        
        if not z.isdigit() and check == False:
            await message.channel.send("😢 hey this wasn't a zipcode")
        elif z.isdigit() and check == False:
            try:
                x = current(z)
                check = True
            except:
                await message.channel.send("😞 hey that isn't a valid ***US ZIPCODE***")
            
            if check:
                
                throw = ""
                    
                if x[7] == "":
                    x[7] = "Visibility is perfect!"
                embed=discord.Embed(title="Current Conditions For {}:".format(x[0]), description="{}{}{}{}{}{}{}{}{}{}{}{}".format(x[5].replace("N/A",x[1]),"\n",x[6].replace("N/A","None"),"\n",x[7].replace("N/A","None"),"\n",x[8].replace("N/A","None"),"\n",x[9].replace("N/A","None"),"\n",x[10].replace("N/A","None"),"\n",), color=0x00ffff)
                embed.set_thumbnail(url=x[2])
                await message.channel.send(embed=embed) 
#_________________________________________________________________
#________________Help Command_____________________________________


      
    if message.content.startswith("(debug 124)"):
        x = message.content.replace("(debug 124)","")
        await client.change_presence(status=discord.Status.online, activity=discord.Game(x))
    
    
    elif message.content == "<@590438181762105344>":
        name = "**{}**".format(message.mentions[0].name)
        command1 = "**~Weather** (us zipcode)"
        command2 = "**~Conditions** (us zipcode)"
        command3 = "**~Forecast** (us zipcode)"
        command4 = "**~Alerts** (us zipcode)"
        Helpmessage = """
        **Thanks for adding me to {}**!
        
        ***Description***
        I am able to tell you about the current weather, forecast, weather alerts, and exact conditions in any US city. :sunny:
        
        ***Commands***
        {}
        {}
        {}
        {}
        
        ***Support The Creator***
        Please support the creator by sharing me to other servers using the following link: 
https://discordapp.com/api/oauth2/authorize?client_id=590438181762105344&permissions=0&scope=bot
        or through the following links.
        -<:patreon:630306170791395348> https://www.patreon.com/b9king
        -<:paypal:630306883105849354> https://www.paypal.com/paypalme2/b9king
        Or you can visit him here: https://benignking.xyz :heart:
        """.format(message.guild.name,command1,command2,command3,command4)
        
        embed=discord.Embed(title="", url="https://www.patreon.com/b9king", description= Helpmessage, color=0x00ffff)
        embed.set_thumbnail(url= message.mentions[0].avatar_url)
        await message.channel.send(embed=embed)   
            

        

                
    
    
#['Death Valley, California, United States',
 #'112°F',
 #'https://d2hhjsu0v3gh4o.cloudfront.net/reports/images/aeris1410/na.gif',
 #'There are currently no weather advisories!',
 #'NONE',
 #'Feels Like 112°F', #condition
 #'Humidity 10%', #condition
 #'', #visibility
 #'Dew Point 43°F', #condition
 #'Wind S 3 MPH Gusts 6', #condition
 #'Barometer N/A', #condition
 #'Day: Sunny. Highs around 89°F. Northwest wind 8 to 18 MPH. ',
 #'https://d2hhjsu0v3gh4o.cloudfront.net/reports/images/aeris1410/sunny.png']


#name = "**:sunny: Weather Bot :cloud_rain:**"
#command1 = "~Weather (zipcode)"
#command2 = "~Stats (zipcode)"
#command3 = "~Forcast (zipcode"
#command4 = "~Alerts (zipcode)"
                
                
client.run('NTkwNDM4MTgxNzYyMTA1MzQ0.XQiPKA.wk3_drQT5NYEiQOqGfNCsyBaDmA') 

