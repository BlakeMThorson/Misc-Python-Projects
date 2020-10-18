
import discord
import random
from asd import *
from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog   

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
        
    
    #_________________________________________________________________   
    #__________________MTG CARD INFO__________________________________
    
    if message.content.startswith("~Price"):
        
        message.content = message.content.replace("~Price ","")
        
        x = cardPrice(message.content)
        
        
        prices = ""
        
        for i in x["prices"]:
            prices += i + "\n"
        
        #
        
        embed=discord.Embed(title= x["name"], description = prices , color=0x746A69)
        embed.set_thumbnail(url= "http://www.manaleak.com/mtguk/files/2012/12/mtg-money.jpg")
        await message.channel.send(embed=embed)        
        
    
    
    if message.content.startswith("~Card "):
        
        await message.channel.send("I'm working on it")

        message.content = message.content.replace("~Card ", "")

        cards = Card.where(name=message.content).all()
        
        color = {"White" : 0xd2d2c1, "Green" : 0x008000, "Black" : 0x000000 , "Red" : 0xff0000 , "Blue" : 0x0080c0 , "None" : 0x808080}
        if len(cards[0].colors) > 0:
            c = cards[0].colors[0]
        else:
            c = "None"
        
        cost = ""
        manas = { "9" : "<:9_:549923808560021505>", "8" : "<:8_:549923808291848194>", "7" : "<:7_:549923035289878558>", "6" : "<:6_:549923035294072847>", "5" : "<:5_:549923035289878548>", "4" : "<:4_:549923035302592512>", "3" : "<:3_:549923035486879744>", "2" : "<:2_:549923035298136104>", "1" : "<:1_:549923035306655744>", "0" : "<:0_:549923035998715914>","X" : "<:x_:549923035382022145>","W" : "<:White:549913967762341888>","B" : "<:Black:549911363607199754>","U" : "<:Blue:549913606347816961>","R" : "<:Red:549910969149816842>","G" : "<:Green:549911048925347850>"} 
        if cards[0].mana_cost != None:
            for i in cards[0].mana_cost:
                if i in manas:
                    cost = cost + manas[i]
         
        desc = cards[0].text
        desc = desc.replace("{W}","<:White:549913967762341888>")
        desc = desc.replace("{B}","<:Black:549911363607199754>")
        desc = desc.replace("{U}","<:Blue:549913606347816961>")
        desc = desc.replace("{R}", "<:Red:549910969149816842>")
        desc = desc.replace("{G}","<:Green:549911048925347850>")
        desc = desc.replace("{X}","<:x_:549923035382022145>") 
        desc = desc.replace("{9}" , "<:9_:549923808560021505>")
        desc = desc.replace("{8}" , "<:8_:549923808291848194>")
        desc = desc.replace("{7}" , "<:7_:549923035289878558>")
        desc = desc.replace("{6}" , "<:6_:549923035294072847>")
        desc = desc.replace("{5}" , "<:5_:549923035289878548>")
        desc = desc.replace("{4}" , "<:4_:549923035302592512>")
        desc = desc.replace("{3}" , "<:3_:549923035486879744>")
        desc = desc.replace("{2}" , "<:2_:549923035298136104>")
        desc = desc.replace("{1}" , "<:1_:549923035306655744>")
        desc = desc.replace("{C}" , "<:1_:549923035306655744>")
        desc = desc.replace("{0}" , "<:0_:549923035998715914>")
        desc = desc.replace("{T}" , "<:tap:549932371806388259>")
        desc = desc.replace("{1}" , "<:1_:549923035306655744>")
        

        
        embed = discord.Embed(
            title = cards[0].name + " " + cost,
            colour = color[c]
            )
        
        legal = ""
        for i in cards[0].legalities:
            legal = legal + i["format"] + " : "
            if i["legality"] == "Legal":
                legal = legal + "✅"
            else:
                legal = legal + "🚫"
            legal = legal + "\n"
            
        rules = ""
        for i in cards[0].rulings:
            rules = rules + i["date"] + " : " + i["text"]
            rules = rules + "\n"
                
        
        
        embed.set_image(url = cards[0].image_url) #card picture
        
        embed.add_field(name = "Text", value =  desc, inline = False) #copy pasta for card info
        
        if cards[0].flavor != None:
            embed.add_field(name = "Flavor", value = cards[0].flavor, inline = False) #copy pasta for card info
        
        if cards[0].power != None:
            embed.add_field(name = "Power/Toughness", value = cards[0].power + "/" + cards[0].toughness , inline = False) #copy pasta for card info
        
        if cards[0].type != None:
            embed.add_field(name = "Type", value = cards[0].type  , inline = False) #copy pasta for card info        
        
        if cards[0].set_name != None: 
            embed.add_field(name = "Set", value =  cards[0].set_name, inline = False) #copy pasta for card info
       
        if cards[0].rarity != None:
            embed.add_field(name = "Rarity", value =  cards[0].rarity, inline = False) #copy pasta for card info
       
        if cards[0].loyalty != None:
            embed.add_field(name = "Loyalty", value =  cards[0].loyalty, inline = False) #copy pasta for card info
        
               
        if cards[0].artist != None:
            embed.add_field(name = "Artist", value =  cards[0].artist, inline = False) #copy pasta for card info
        
                  
        if cards[0].variations != None:
            embed.add_field(name = "Variations", value =  cards[0].variations, inline = False) #copy pasta for card info
            
        
        if cards[0].release_date != None:
            embed.add_field(name = "Release Date", value =  cards[0].release_date, inline = False) #copy pasta for card info
        
                   
        if rules != None and len(rules) != 0:
            embed.add_field(name = "RULINGS", value = rules, inline = False) #copy pasta for card info
        
        
        if cards[0].legalities != None:
            embed.add_field(name = "Legalities", value =  legal , inline = False) #copy pasta for card info        
        
        
        embed.set_footer(text="Coded by : B9king", icon_url="https://cdn6.aptoide.com/imgs/8/2/3/823240ba13a239948950f78f38b1f1d9_icon.png?w=256") #My credit
        
        
        await message.channel.send(embed=embed) 




client.run('NjM1NTk0MzE3MDAzNjIwMzYy.XazWfA.7KMudkJo_OD7R9UpAt1Rv55ipCs')