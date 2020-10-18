import discord
import random

client=discord.Client()



#OLD BOTS
from asd import *
from MOVIEHELPER import *
from weatherHelper import *

def weedFormatting(d):
    effects = ['😌 Relaxed', '🍔 Hungry', '😃 Happy', '😴 Sleepy', '🤯 Euphoric', '🎭 Creative', '🏃🏻 Energetic', '📱 Talkative', '😜 Arouse', '🤲 Uplifted', '😐 Focused', '🤣 Giggly', '😵 Dizzy', '😨 Paranoid', '😰 Anxious', '🙂 Tingly', '👄 Dry Mouth']
    
    flav =    ['🌱 Earthy', '🧪 Chemical', '🎄 Pine', '🌿 Spicy/Herbal', '💪 Pungent', '🌶️ Pepper', '🌼 Flowery', '🍋 Citrus', '🍊 Orange', '🍬 Sweet', '🦨 Skunk', '🌳 Woody', '🍇 Grape', '🍬 Minty', '🧀 Cheese', '⛽ Diesel', '🌴 Tropical', '🍊 Grapefruit', '🥜 Nutty', '🍋 Lemon', '🍓 Berry', '💙 Blueberry', '🧪 Ammonia', '🍎 Apple', '🌹 Rose', '🧈 Butter', '🥭 Mango', '🍯 Honey', '🍵 Tea', '💚 Lime', '💜 Lavender', '🍓 Strawberry', '🍬 Mint', 'Chestnut', '🌴 Tree Fruit', '🍐 Pear', '🧡 Apricot', '🍑 Peach', '🧀 Blue Cheese', '🚬 Menthol', '☕ Coffee', '🚬 Tar', '🍍 Pineapple', '🌿 Sage', '🍦 Vanilla', '💜 Plum', '🚬 Tobacco', '💜 Violet']
    positive = ""
    negative = ""
    flavors = ""
    for i in d["effects"]["positive"] :
        for new in effects:
            if i in new:
                positive += "{}\n".format(new)
    for i in d["effects"]["negative"] :
        for new in effects:
            if i in new:
                negative += "{}\n".format(new)
    for i in d["flavors"]:
        for new in flav:
            if i in new:
                flavors += "{}\n".format(new)                
    toSend = """**Flavors**: 
{}
**Effects**:
*Positive*:
{}
*Negative*:
{}""".format(flavors,positive,negative)
    #print(toSend)
    return toSend



def getByName(name):
    from imdb import IMDb
    ia = IMDb() 
    x = name
    z = ia.search_movie(x)
    z = ia.get_imdbID(z[0])
    ID = z
    z = ia.get_movie(z)     
    g = int(z.get('rating'))
    stars = "⭐" * g
    stars += "<:estar:628099467320492032>" * (10-g)    
    return [z,stars, ID]

def getByID(ID):
    
    ID = ID.replace("tt","")
    
    from imdb import IMDb
    ia = IMDb() 
    z = ia.get_movie(ID) 
    g = int(z.get('rating'))
    stars = "⭐" * g
    stars += "<:estar:628099467320492032>" * (10-g)    
    return [z,stars]


#normal bot
@client.event
async def on_ready():
    ##print('logged in as')
    ##print(client.user.name)
    ##print(client.user.id)
    ##print('-----')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("B9king Jr Jr"))
    
@client.event
async def on_message(message):
    message.content = message.content.lower()
    
#=========================================================================================================
#=========================================================================================================
#                                       OTHER BOTS
#=========================================================================================================
#=========================================================================================================
   
   #---------------------------------------------------------------------------------------------------- 

   #----------------------------------------------------------------------------------------------------  
    if message.content.startswith("~taco"):
        x = Taco()
        taco = "{}".format(x["recipe"])
        embed=discord.Embed(title= "The Taco Bot's Hottest : " , color=0xfce21b, description = taco , url = x["url"])
        embed.set_thumbnail(url="https://files.catbox.moe/prc9ze.gif")
        embed.set_footer(text="🌎 BenignKing.xyz - Paypal.me/B9king - Patreon.com/B9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")
        await message.channel.send(embed=embed)      
#---------------------------------------------------------------------------------------------------- 
    if message.content.startswith("~cat"):
        embed=discord.Embed(title= catFacts() , color=0x746A69)
        embed.set_author(name="CAT FACT:")
        embed.set_thumbnail(url="https://i.pinimg.com/originals/dc/d7/03/dcd70309b118dfbcce7689886fae9a38.gif")
        embed.set_footer(text="🌎 BenignKing.xyz - Paypal.me/B9king - Patreon.com/B9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")
        await message.channel.send(embed=embed)   
 #---------------------------------------------------------------------------------------------------- 
    if message.content.startswith("~search "):
        message.content = message.content.replace("~search ", "")
        fuckYou = getByName(message.content)
        z = fuckYou[0]
        stars = fuckYou[1]
        dumpt = formatter(z.get('genre'))
        genre = ""
        for i in dumpt:
            genre += i + "\n"
        #summary
        summary = z.get('plot')[0]
        summary = summary[:700] 
        try:
            summary = summary[:summary.index(".::")]
        except:
            pass
        summary += "..."
        embed = discord.Embed(
            title = str(z.get('title')),
            url = "https://www.imdb.com/title/tt{}".format(fuckYou[2]),
            color=0xf0ffff,
            )
        embed.add_field(name = "Rating", value = stars , inline = False )
        embed.add_field(name = "Genre", value = str(genre) , inline = False)
        embed.set_thumbnail(url = str(z.get('cover')))
        embed.add_field(name = "Summary", value = summary, inline = False)
        embed.set_footer(text="🌎 BenignKing.xyz - Paypal.me/B9king - Patreon.com/B9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")

        await message.channel.send(embed=embed)            
    ##print random genres
    
#---------------------------------------------------------------------------------------------------- 
    elif message.content.startswith("~genres"):
        x = """<:action:643387530170990610> Action
<:adult:643387530586357760> Adult
<:adventure:643387530582032384> Adventure
<:animation:643387530573512714> Animation
<:biography:643387530351476747> Biography
<:comedy:643387530523312149> Comedy
<:crime:643387530594484224> Crime
<:documentary:643387530691215360> Documentary
<:drama:643387530594615336> Drama
<:family2:643387530255007756> Family
<:fantasy:643387530229579778> Fantasy
<:filmnoir:643387530678370304> Film-Noir
<:history:643387530640752660> History
<:horror:643387530716250112> Horror
<:music:643387530691084318> Music
<:music:643387530691084318> Musical
<:mystery:643387530682564609> Mystery
<:news:643387530707730441> News
<:realitytv:643387530838016001> Reality-TV
<:romance:643387530699603978> Romance
<:scifi:643387531085217802> Sci-Fi
<:short:643387530359865345> Short
<:sport:643387530724638750> Sport
<:thriller:643387530909188116> Thriller
<:war:643387530942742539> War
<:western:643387530531700748> Western"""
        
        
        embed=discord.Embed()
        embed.add_field(name="Genres", value=x, inline=False)
        embed.set_footer(text="🌎 BenignKing.xyz - Paypal.me/B9king - Patreon.com/B9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")
        await message.channel.send(embed=embed)        
 #----------------------------------------------------------------------------------------------------        
    elif message.content == ("~random"):
        fuck = trueRandom()
        image = fuck["poster_400x570"]
        fuckYou = getByID(fuck["imdb"])
        z = fuckYou[0]
        stars = fuckYou[1]
        dumpt = formatter(z.get('genre'))
        genre = ""
        for i in dumpt:
            genre += i + "\n"
        #summary
        summary = z.get('plot')[0]
        summary = summary[:700]
        summary = summary[:summary.find("::")]
        summary += "..."
        embed = discord.Embed(
            title = str(z.get('title')),
            url = "https://www.imdb.com/title/{}".format(fuck["imdb"]),
            color=0xf0ffff,
            )
        embed.add_field(name = "Rating", value = stars , inline = False )
        embed.add_field(name = "Genre", value = str(genre) , inline = False)
        embed.set_thumbnail(url = image)
        embed.add_field(name = "Summary", value = summary, inline = False)
        embed.set_footer(text="🌎 BenignKing.xyz - Paypal.me/B9king - Patreon.com/B9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")
        await message.channel.send(embed=embed)          
#----------------------------------------------------------------------------------------------------      
    #get random movie based on genre
    elif message.content.startswith("~get "):
        fuck = getMovie( message.content.replace("~get ","") ) 
        image = fuck["poster_400x570"]
        fuckYou = getByID(fuck["imdb"])
        z = fuckYou[0]
        stars = fuckYou[1]
        dumpt = formatter(z.get('genre'))
        genre = ""
        for i in dumpt:
            genre += i + "\n"
        #summary
        summary = z.get('plot')[0]
        summary = summary[:700]
        summary = summary[:summary.find("::")]
        summary += "..."
        embed = discord.Embed(
            title = str(z.get('title')),
            url = "https://www.imdb.com/title/{}".format(fuck["imdb"]),
            color=0xf0ffff,
            )
        embed.add_field(name = "Rating", value = stars , inline = False )
        embed.add_field(name = "Genre", value = str(genre) , inline = False)
        embed.set_thumbnail(url = image)
        embed.add_field(name = "Summary", value = summary, inline = False)
        embed.set_footer(text="🌎 BenignKing.xyz - Paypal.me/B9king - Patreon.com/B9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")
        await message.channel.send(embed=embed)   
 #----------------------------------------------------------------------------------------------------    
    if message.content.startswith("~drink"):
        message.content = message.content.replace("~drink ","")
        try:
            x = ingredientSearch(message.content)
            embed=discord.Embed(title= x["ingredients"] , color=0x746A69, description = x["recipe"])
            embed.set_author(name= x["name"])
            embed.set_thumbnail(url=x["image"])
            embed.set_footer(text="🌎 BenignKing.xyz - Paypal.me/B9king - Patreon.com/B9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")
            await message.channel.send(embed=embed)        
        except:
            await message.channel.send("COULDN'T FIND THAT INGREDIENT")
#----------------------------------------------------------------------------------------------------   
    if message.content.startswith("~all effects"):
        toSend = """
Please type ~Effect (effect name) to get a random strain of weed.
    
Positive:
  😌 Relaxed
  🍔 Hungry
  😃 Happy
  😴 Sleepy
  🤯 Euphoric
  🎭 Creative
  🏃🏻 Energetic
  📱 Talkative
  😜 Arouse
  🤲 Uplifted
  😐 Focused
  🤣 Giggly
        
Negative:
  😵 Dizzy
  😨 Paranoid
  😰 Anxious
  🙂 Tingly
  👄 Dry Mouth
        """
        await message.channel.send(toSend)
 #----------------------------------------------------------------------------------------------------         
    if message.content.startswith("~effect"):
        message.content = message.content.replace("~effect ","")   
        message.content = message.content.capitalize()
        with open('WEED_EFFECTS.pickle', 'rb') as handle:
            b = pickle.load(handle)
        if message.content not in b.keys():
            await message.channel.send("Hey that wasn't a valid choice my dude, please try again")
        else:
            g = random.choice(b[message.content])
            nama = g["name"]
            g = weedFormatting(g)
            embed=discord.Embed(title= "" , color=0x7BAA47)
            embed.add_field(name= nama, value= g, inline=False)
            embed.set_thumbnail(url="http://giphygifs.s3.amazonaws.com/media/4LlTwUsF6M8Sc/giphy.gif")
            embed.set_footer(text="🌎 BenignKing.xyz - Paypal.me/B9king - Patreon.com/B9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")
            await message.channel.send(embed=embed)            
        with open('WEED_FLAVORS.pickle', 'rb') as handle:
            b = pickle.load(handle)
            
#----------------------------------------------------------------------------------------------------              
    if message.content.startswith("~all flavors"):
        flavors = """**Type ~Flavor (flavor name) to get a random strain of that flavor**
**Fruit**
🍋 Citrus
🍊 Orange
🍋 Lemon
🍓 Berry
🌴 Tropical
🍊 Grapefruit
💙 Blueberry
🍎 Apple
🥭 Mango
🍐 Pear
🧡 Apricot
🍑 Peach
🌴 Tree Fruit
🍇 Grape
💚 Lime
🍓 Strawberry
🍍 Pineapple
💜 Plum

**Sweet**
🍬 Sweet
🍯 Honey
🍬 Minty
🍬 Mint

**Earthy**
🌱 Earthy
🎄 Pine
🌿 Spicy/Herbal
🌼 Flowery
🌹 Rose
💜 Lavender
🌳 Woody
🌿 Sage
💜 Violet

**Food & Drink**
🌶️ Pepper
🧀 Cheese
🥜 Nutty
🧈 Butter
🍵 Tea
🌰 Chestnut
🧀 Blue Cheese
☕ Coffee
🍦 Vanilla

**Misc**
💪 Pungent
🦨 Skunk
⛽ Diesel
🧪 Chemical
🧪 Ammonia
🚬 Menthol
🚬 Tar
🚬 Tobacco
"""
        await message.channel.send(flavors)
#----------------------------------------------------------------------------------------------------  
    if message.content.startswith("~flavor"):
        message.content = message.content.replace("~flavor ","")  
        message.content = message.content.capitalize()
        with open('WEED_FLAVORS.pickle', 'rb') as handle:
            b = pickle.load(handle)
        if message.content not in b.keys():
            await message.channel.send("Hey that wasn't a valid choice my dude, please try again")
        else:
            g = random.choice(b[message.content])
            nama = g["name"]
            g = weedFormatting(g)
            embed=discord.Embed(title= "" , color=0x7BAA47)
            embed.add_field(name= nama, value= g, inline=False)
            embed.set_thumbnail(url="http://giphygifs.s3.amazonaws.com/media/4LlTwUsF6M8Sc/giphy.gif")
            embed.set_footer(text="🌎 BenignKing.xyz - Paypal.me/B9king - Patreon.com/B9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")
            await message.channel.send(embed=embed)            
        with open('WEED_RACES.pickle', 'rb') as handle:
            b = pickle.load(handle)
        with open('allStrains.pickle', 'rb') as handle:
            b = pickle.load(handle)
#----------------------------------------------------------------------------------------------------  
  
#----------------------------------------------------------------------------------------------------  
  
#----------------------------------------------------------------------------------------------------  
            x = current(z)
            check = True
            if x[3] == "There are currently no weather advisories!":
                alert = False
            if check and alert:
                embed=discord.Embed(title="Weather Alerts for {}".format(x[0]), url= x[4] , description="{}".format(x[3]), color=0xff0000)
                embed.set_thumbnail(url="https://ui-ex.com/images/increated-clipart-red-alert-3.png")
                embed.set_footer(text="🌎 BenignKing.xyz - Paypal.me/B9king - Patreon.com/B9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")
                await message.channel.send(embed=embed)
            else:
                embed=discord.Embed(title="There are no alerts for {}:".format(x[0]), description="Let's hope it stays that way!", color=0x00ff00)
                embed.set_thumbnail(url="http://chittagongit.com/download/354591")
                embed.set_footer(text="🌎 BenignKing.xyz - Paypal.me/B9king - Patreon.com/B9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")
                await message.channel.send(embed=embed)
#----------------------------------------------------------------------------------------------------              
            embed=discord.Embed(title="Forecast For {}:".format(x[0]), description="{}".format(x[11]), color=0x00ffff)
            embed.set_thumbnail(url=x[12])
            embed.set_footer(text="🌎 BenignKing.xyz - Paypal.me/B9king - Patreon.com/B9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")
            await message.channel.send(embed=embed)  
#----------------------------------------------------------------------------------------------------  
            if x[7] == "":
                x[7] = "Visibility is perfect!"
            embed=discord.Embed(title="Current Conditions For {}:".format(x[0]), description="{}{}{}{}{}{}{}{}{}{}{}{}".format(x[5].replace("N/A",x[1]),"\n",x[6].replace("N/A","None"),"\n",x[7].replace("N/A","None"),"\n",x[8].replace("N/A","None"),"\n",x[9].replace("N/A","None"),"\n",x[10].replace("N/A","None"),"\n",), color=0x00ffff)
            embed.set_thumbnail(url=x[2])
            embed.set_footer(text="🌎 BenignKing.xyz - Paypal.me/B9king - Patreon.com/B9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")
            await message.channel.send(embed=embed) 
#_________________________________________________________________      
    elif "corona" in message.content: #{'cases': '2,770', 'deaths': '80', 'notes': '', 'url': ''}
        if "mobile" not in message.content:

            #GET VARIABLES
            g = newCorona()
            #make the fucking table
            info = g[1]
            x = g[0]
            
            faces = ["😷","🤢","🤮"]
            skulls = ["💀"]
            toReturn = ""
            
            gifs = ["https://media.giphy.com/media/55itGuoAJiZEEen9gg/giphy.gif","https://media2.giphy.com/media/3oKIP657aH5QRMkX3q/giphy.gif","https://media1.giphy.com/media/H7naQrujHfaZW/giphy.gif","https://66.media.tumblr.com/72ee1af05ac70a08dd44d11581d249da/tumblr_p4bft8xEvk1r6rzrwo1_400.gifv"]
            
            
            if len(info["New"]) > 0:
                embed=discord.Embed(title="CORONA HAS SPREAD!", color=0xc0392b, description = toReturn)
                embed.set_thumbnail(url= random.choice(gifs) ) 
                embed.add_field(name= "THE PLAGUE HAS BEEN DISCOVERED IN", value= "{}".format(" ".join(str(i) for i in info["new"] )) , inline=True)
                embed.set_footer(text="MADE BY B9KING#6857", icon_url = "https://files.catbox.moe/4xckm3.PNG")
                await message.channel.send(embed=embed)               
            
            new = []
            
            for i in list(x.keys()):
                if "cases change" not in x[i] and i != "last update":
                    new.append(i)
                    
                    
            if len(new) > 0:
                embed=discord.Embed(title="CORONA HAS SPREAD!", color=0xc0392b, description = toReturn)
                embed.set_thumbnail(url= random.choice(gifs) ) 
                embed.add_field(name= "THE PLAGUE HAS BEEN DISCOVERED IN", value= "{}".format(" , ".join(str(i) for i in new)) , inline=True)
                embed.set_footer(text="MADE BY B9KING#6857", icon_url = "https://files.catbox.moe/4xckm3.PNG")
                await message.channel.send(embed=embed)            
        
            
            #g[0]["China"]
            #{'cases': '9,694', 'deaths': '213', 'notes': '', 'url': 'https://www.cnn.com/asia/live-news/coronavirus-outbreak-01-27-20-intl-hnk/index.html', 'death change': ':chart_with_downwards_trend:0', 'cases change': ':chart_with_downwards_trend:0'}
            
            
            #g[1]
            #{'Totals': '9,822 confirmed cases worldwide, including 213 fatalities.', 'New': []}        
           
            date = x["last update"]
            
            #start the embed
            embed=discord.Embed(title="CORONA VIRUS STATS:\n{}\n{}".format(date,info["Totals"]), color=0xc0392b, description = toReturn)
            embed.set_thumbnail(url="https://files.catbox.moe/k7u0p3.png")  
            
            for i in list(x.keys()):
                if i != "last update":
                    try:
                        embed.add_field(name= i, value= "[{} {} {} - {} {} {}]({})".format( random.choice(faces) , x[i]["cases"], x[i]["cases change"] , random.choice(skulls), x[i]["deaths"], x[i]["death change"] ,x[i]["url"])  , inline=True)            
                    except:
                        embed.add_field(name= "NEW : {}".format(i), value= "[{} {} - {} {}]({})".format( random.choice(faces) , x[i]["cases"], random.choice(skulls), x[i]["deaths"], x[i]["url"])  , inline=True)           
                           
        
            embed.set_footer(text="MADE BY B9KING#6857", icon_url = "https://files.catbox.moe/4xckm3.PNG")
            await message.channel.send(embed=embed)        
            
            #IF THEY DONT EXIST SHARE THE RESULTS
        
        else:
 
            #GET VARIABLES
            g = newCorona()
            #make the fucking table
            info = g[1]
            x = g[0]
            
            faces = ["😷","🤢","🤮"]
            skulls = ["💀"]
            toReturn = ""
            
            gifs = ["https://media.giphy.com/media/55itGuoAJiZEEen9gg/giphy.gif","https://media2.giphy.com/media/3oKIP657aH5QRMkX3q/giphy.gif","https://media1.giphy.com/media/H7naQrujHfaZW/giphy.gif","https://66.media.tumblr.com/72ee1af05ac70a08dd44d11581d249da/tumblr_p4bft8xEvk1r6rzrwo1_400.gifv"]
            
            try:
                if len(info["New"]) > 0:
                    embed=discord.Embed(title="CORONA HAS SPREAD!", color=0xc0392b, description = toReturn)
                    embed.set_thumbnail(url= random.choice(gifs) ) 
                    embed.add_field(name= "THE PLAGUE HAS BEEN DISCOVERED IN", value= "{}".format(" ".join(str(i) for i in info["new"] )) , inline=True)
                    embed.set_footer(text="MADE BY B9KING#6857", icon_url = "https://files.catbox.moe/4xckm3.PNG")
                    await message.channel.send(embed=embed)      
            
            except:
                pass
                
            new = []
            
            for i in list(x.keys()):
                if "cases change" not in x[i] and i != "last update":
                    new.append(i)
                    
                    
            if len(new) > 0:
                embed=discord.Embed(title="CORONA HAS SPREAD!", color=0xc0392b, description = toReturn)
                embed.set_thumbnail(url= random.choice(gifs) ) 
                embed.add_field(name= "THE PLAGUE HAS BEEN DISCOVERED IN", value= "{}".format(" , ".join(str(i) for i in new)) , inline=True)
                embed.set_footer(text="MADE BY B9KING#6857", icon_url = "https://files.catbox.moe/4xckm3.PNG")
                await message.channel.send(embed=embed)            
        
            
            #g[0]["China"]
            #{'cases': '9,694', 'deaths': '213', 'notes': '', 'url': 'https://www.cnn.com/asia/live-news/coronavirus-outbreak-01-27-20-intl-hnk/index.html', 'death change': ':chart_with_downwards_trend:0', 'cases change': ':chart_with_downwards_trend:0'}
            
            
            #g[1]
            #{'Totals': '9,822 confirmed cases worldwide, including 213 fatalities.', 'New': []}        
           
            date = x["last update"]
            
            #start the embed
            embed=discord.Embed(title="CORONA VIRUS STATS:\n{}\n{}".format(date,info["Totals"]), color=0xc0392b, description = toReturn)
            embed.set_thumbnail(url="https://files.catbox.moe/k7u0p3.png")  
            
            toReturn = ""
            
            for i in list(x.keys()):
                if i != "last update":
                    try:
                        toReturn += "{} : {} {} {} - {} {} {}\n\n".format(i,random.choice(faces) , x[i]["cases"], x[i]["cases change"] , random.choice(skulls), x[i]["deaths"], x[i]["death change"])         
                    except:
                        toReturn += "**NEW** {} : {} {} - {} {}\n".format(i,random.choice(faces) , x[i]["cases"], random.choice(skulls), x[i]["deaths"])           
            
            
            
            embed.add_field(name= "INFECTED AREAS:", value= "{}".format(toReturn[:1020])  , inline=True)
            embed.add_field(name= "INFECTED AREAS:", value= "{}".format(toReturn[1020:])  , inline=True)
 
        
            embed.set_footer(text="MADE BY B9KING#6857", icon_url = "https://files.catbox.moe/4xckm3.PNG")
            await message.channel.send(embed=embed)        
           
           #IF THEY DONT EXIST SHARE THE RESULTS            
            
        
        #IF THEY DONT EXIST SHARE THE RESULTS

















































#=========================================================================================================
#=========================================================================================================
#                                       BANKING AND MONEY 
#=========================================================================================================
#=========================================================================================================

#----------------------------------------------------------------------------------------------------
#--------------------------JOIN THE GAME-------------------------------------------------------------
#----------------------------------------------------------------------------------------------------  
    if message.content == "~add me":
        #GET VARIABLES
        name = message.author.name
        ID = message.author.id
        #CREATE ENTRY
        g = createUser(name,ID)
        #IF THEY EXIST
        if g == "YOU ARE ALREADY IN THERE":
            embed=discord.Embed(title="😛 You're already banking with us silly ~!", color=0xc0392b, description = "You can check you balance with ~Balance")
            embed.set_author(name="The Bank Of {}".format(message.guild.name))
            embed.set_thumbnail(url="https://files.catbox.moe/4m3oh3.png")
            await message.channel.send(embed=embed)        
        #IF THEY DONT EXIST SHARE THE RESULTS
        else:
            embed=discord.Embed(title="Your current balance is $1000", color=0x27ae60, description = "Thanks so much for choosing to bank with us 💕 ~!")
            embed.set_author(name="Welcome To The Bank Of {}".format(message.guild.name))
            embed.set_thumbnail(url="https://files.catbox.moe/4m3oh3.png")
            await message.channel.send(embed=embed)    
#----------------------------------------------------------------------------------------------------
#--------------------------CHECK YOUR BALANCE--------------------------------------------------------
#----------------------------------------------------------------------------------------------------  
    elif message.content == "~balance":
        #Get Variables
        ID = message.author.id
        #GET BALANCE
        g = checkBalance(ID)
        if g == "YOU DONT EXIST":
            embed=discord.Embed(title="😕 I can't seem to find you in the system.", color=0xc0392b, description = "If you wish to become a new customer you can type ~add me and I'll put you in the system right away ~!")
            embed.set_author(name="The Bank Of {}".format(message.guild.name))
            embed.set_thumbnail(url="https://files.catbox.moe/4m3oh3.png")    
        else:
            embed=discord.Embed(title="Your current balance is ${:,}".format(g), color=0x27ae60, description = "Thanks so much for choosing to bank with us 💕 ~!")
            embed.set_author(name="Welcome To The Bank Of {}".format(message.guild.name))
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/665179204576608279/665187370521460746/default.png")
            await message.channel.send(embed=embed)           

#----------------------------------------------------------------------------------------------------
#--------------------------CHECK YOUR BALANCE--------------------------------------------------------
#----------------------------------------------------------------------------------------------------
    elif message.content == "~bal":
        #Get Variables
        ID = message.author.id
        #GET BALANCE
        g = checkBalance(ID)
        if g == "YOU DONT EXIST":
            embed=discord.Embed(title="😕 I can't seem to find you in the system.", color=0xc0392b, description = "If you wish to become a new customer you can type ~add me and I'll put you in the system right away ~!")
            embed.set_author(name="The Bank Of {}".format(message.guild.name))
            embed.set_thumbnail(url="https://files.catbox.moe/4m3oh3.png")    
        else:
            embed=discord.Embed(title="Your current balance is ${:,}".format(g), color=0x27ae60, description = "Thanks so much for choosing to bank with us 💕 ~!")
            embed.set_author(name="Welcome To The Bank Of {}".format(message.guild.name))
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/665179204576608279/665187370521460746/default.png")
            await message.channel.send(embed=embed)           
        
#----------------------------------------------------------------------------------------------------
#--------------------------PAY SOMEONE MONEY---------------------------------------------------------
#----------------------------------------------------------------------------------------------------     
    elif message.content.startswith("~pay"):
        fuck = message.content.index(">")
        toPay = message.mentions[0].id
        name = message.mentions[0].name
        paying = message.author.id
        
        if paying != toPay:
            message.content = message.content[fuck:]
            message.content = message.content.replace(">", "")
            message.content = message.content.replace(" ","")
            message.content = int(message.content)
            ##print(message.content)
            pay(paying, toPay, message.content)
            
            embed=discord.Embed(title="You've paid {} ${}".format(name,str(message.content)), color=0x27ae60, description = "I'm sure they are really happy to recieve it💕 ~!")
            embed.set_author(name="Welcome To The Bank Of {}".format(message.guild.name))
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/665179204576608279/665187370521460746/default.png")
            await message.channel.send(embed=embed)        
            
#----------------------------------------------------------------------------------------------------
#--------------------------TAKE OUT A LOAN-----------------------------------------------------------
#----------------------------------------------------------------------------------------------------    
    elif message.content.startswith("~borrow"):
        amount = message.content.replace("~borrow","")
        amount = amount.replace(" ","")
        amount = int(amount)
        ID = message.author.id
        takeLoan(ID,amount)
        
        x = getLoan(ID)
        #if they aren't in the system
        if x == "YOU DONT EXIST":
            embed=discord.Embed(title="😕 I can't seem to find you in the system.", color=0xc0392b, description = "If you wish to become a new customer you can type ~add me and I'll put you in the system right away ~!")
            embed.set_author(name="The Bank Of {}".format(message.guild.name))
            embed.set_thumbnail(url="https://files.catbox.moe/4m3oh3.png")
            await message.channel.send(embed=embed)      
                        
       #if they tried to borrow to much money
        elif x == "I can't loan you that":
            embed=discord.Embed(title="😕 I can only loan out $100,000 at a time to a single person.", color=0xc0392b, description = "This does include your current loan of ${}, \n You can always repay your loan using ~repay AMOUNT if you need another loan.".format(getLoan(ID)))
            embed.set_author(name="The Bank Of {}".format(message.guild.name))
            embed.set_thumbnail(url="https://files.catbox.moe/4m3oh3.png")
            await message.channel.send(embed=embed)  
        elif x ==  "You've borrowed too much!":
            embed=discord.Embed(title="😕 I can only loan out $100,000 at a time to a single person.", color=0xc0392b, description = "This does include your current loan of ${}, \n You can always repay your loan using ~repay AMOUNT if you need another loan.".format(getLoan(ID)))
            embed.set_author(name="The Bank Of {}".format(message.guild.name))
            embed.set_thumbnail(url="https://files.catbox.moe/4m3oh3.png")
            await message.channel.send(embed=embed)      
                
                        
        #if they are good to go
        else:
            embed=discord.Embed(title="Your total loan amount is ${:,}".format(x), description="*You can do ~repay AMOUNT anytime you want to pay me back ~ !*", color=0xF79F1F)
            embed.set_author(name="You have taken a loan for ${:,}".format(amount))
            embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/SJsbHLuIOG7u_6det7wV9QXunOdIt7blwRciX5T989o/https/media.discordapp.net/attachments/665179204576608279/665187370521460746/default.png")
            await message.channel.send(embed=embed)      
            
        
#----------------------------------------------------------------------------------------------------
#--------------------------REPAY YOUR LOANS----------------------------------------------------------
#----------------------------------------------------------------------------------------------------
    elif message.content.startswith("~repay"):
        ID = message.author.id
        y = getLoan(ID)
        amount = message.content.replace("~repay","")
        amount = amount.replace(" ","")
        amount = int(amount)

        payLoan(ID,amount)
        
        x = getLoan(ID)
        
        if x != y:
            embed=discord.Embed(title="Your total loan amount is ${}".format(x), description="*You can feel free to ~borrow some more ~ !*", color=0xF79F1F)
            embed.set_author(name="You have paid ${} of your loan".format(amount))
            embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/SJsbHLuIOG7u_6det7wV9QXunOdIt7blwRciX5T989o/https/media.discordapp.net/attachments/665179204576608279/665187370521460746/default.png")
            await message.channel.send(embed=embed)
        else:
            message.channel.send("IM UNABLE TO PROCESS DUE TO LACK OF FUNDS")


#----------------------------------------------------------------------------------------------------
#--------------------------REPAY YOUR LOANS----------------------------------------------------------
#----------------------------------------------------------------------------------------------------
    elif message.content.startswith("~check loan"):
        ID = message.author.id
        y = getLoan(ID)
        embed=discord.Embed(title="Your total loan amount is ${:,}".format(y), color=0xF79F1F)
        embed.set_author(name="Welcome to the Bank Of {}".format(message.guild.name))
        embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/SJsbHLuIOG7u_6det7wV9QXunOdIt7blwRciX5T989o/https/media.discordapp.net/attachments/665179204576608279/665187370521460746/default.png")
        await message.channel.send(embed=embed)

            
                    
        

#=========================================================================================================
#=========================================================================================================
#                                 GAMBLING AND BANKRUPTCY
#=========================================================================================================
#=========================================================================================================

#----------------------------------------------------------------------------------------------------
#--------------------------Thing that does the races-------------------------------------------------
#----------------------------------------------------------------------------------------------------
    elif message.content.startswith("~race"):
        ##print("detected ~race")
        #get amount bet:
        amount = message.content.replace("~race ", "")
        amount = amount.replace(" ","")
        #check if it's a number
        if amount.isdigit():
            ##print("detected bet")
            #set it to an int
            amount = int(amount)
            #Get Variables
            ID = message.author.id
            #GET BALANCE
            g = checkBalance(ID)
            
            #check if the balance < bet:
            if g < amount:
                await message.channel.send("YOU CANNOT AFFORD THAT BET, THIS TEXT WILL BE REPLACED WITH AN EMBED SOON")
            #if they have enough money to make the bet, then actually run the race.
            else:
                raceResults = fullRace()
                #{'first': ['unicorn', {'emoji': '<:unicornface:665228779160862750>', 'wins': 72, 'losses': 180}], 'second': ['turtle', {'emoji': '<:turtle:665228779106336789>', 'wins': 43, 'losses': 183}], 'third': ['rabbit', {'emoji': '<:rabbit:665228779198742549>', 'wins': 60, 'losses': 179}], 'fourth': ['sheep', {'emoji': '<:sheep:665228779030839298>', 'wins': 57, 'losses': 178}]}
                
                displayOrder = random.sample(range(0, 4), 4)
                toss = list(raceResults.keys())
                toDisplay = []
                
                for i in displayOrder:
                    toDisplay.append( raceResults[ toss[ i ] ] )
                
                #[['sheep', {'emoji': '<:sheep:665228779030839298>', 'wins': 57, 'losses': 179}], ['snail', {'emoji': '<:snail:665228778942889985>', 'wins': 51, 'losses': 173}], ['goat', {'emoji': '<:goat:665228779047616532>', 'wins': 81, 'losses': 168}], ['rabbit', {'emoji': '<:rabbit:665228779198742549>', 'wins': 60, 'losses': 180}]]
                
                embed=discord.Embed(title="Today's ${:,} Race Features!".format(amount), description="Click The Reactions Below!", color=0x8e44ad)
                embed.add_field(name="{}  **{}**".format(toDisplay[0][1]["emoji"],toDisplay[0][0]), value="{}% of races won".format( str( int( ( toDisplay[0][1]["wins"] / toDisplay[0][1]["losses"] )*100 ) ) ), inline=False)
                embed.add_field(name="{}  **{}**".format(toDisplay[1][1]["emoji"],toDisplay[1][0]), value="{}% of races won".format( str( int( ( toDisplay[1][1]["wins"] / toDisplay[1][1]["losses"] )*100 ) ) ), inline=False)
                embed.add_field(name="{}  **{}**".format(toDisplay[2][1]["emoji"],toDisplay[2][0]), value="{}% of races won".format( str( int( ( toDisplay[2][1]["wins"] / toDisplay[2][1]["losses"] )*100 ) ) ), inline=False)
                embed.add_field(name="{}  **{}**".format(toDisplay[3][1]["emoji"],toDisplay[3][0]), value="{}% of races won".format( str( int( ( toDisplay[3][1]["wins"] / toDisplay[3][1]["losses"] )*100 ) ) ), inline=False)
                await message.channel.send(embed=embed)                
                
                raceEmbed= await message.channel.history().get(author=client.user)
                raceID = raceEmbed.id
                
                choices = {toDisplay[0][1]["emoji"]: "none",
                           toDisplay[1][1]["emoji"]: "none",
                           toDisplay[2][1]["emoji"]: "none",
                           toDisplay[3][1]["emoji"]: "none"}                
                for choice in choices:
                    await raceEmbed.add_reaction(choice)
                #sleep for a little bit
                await asyncio.sleep(10)
                raceEmbed= msg = await message.channel.fetch_message(raceID)
                #GET THE REACTIONS
                dumbass_dict = {}
                for reaction in raceEmbed.reactions:
                    async for user in reaction.users():
                        if user.id not in dumbass_dict:
                            dumbass_dict[user.id] = []
                        dumbass_dict[user.id].append(reaction.emoji)
                winLoss = ""
                #don't check 665208842862460963  
                winner = raceResults["first"][0]
                for i in list( dumbass_dict.keys() ):
                    #make sure it's not the bot
                    if i != 665208842862460963:
                        #make sure they have the money for the bet
                        if checkBalance(i) >= amount * len(dumbass_dict[i]):
                        
                            #go through the bets of each person if it's not the bot
                            for racer in dumbass_dict[i]:
                                
                                if racer.name == winner:
                                    addMoney(i,int(amount))
                                else:
                                    removeMoney(i,int(amount))                        
                raceEmbed= msg = await message.channel.fetch_message(raceID)
                #image links
                icons = {
                    "pig":"https://benignking.xyz/thigns%20for%20bots/pig_1f416.png",
                    "rabbit":"https://neocities.org/dashboard?dir=%2Fthigns+for+bots#",
                    "sheep":"https://benignking.xyz/thigns%20for%20bots/sheep_1f411.png",
                    "snail":"https://benignking.xyz/thigns%20for%20bots/snail_1f40c.png",
                    "turtle":"https://benignking.xyz/thigns%20for%20bots/turtle_1f422.png",
                    "unicorn":"https://benignking.xyz/thigns%20for%20bots/unicorn-face_1f984.png",
                    "chick":"https://benignking.xyz/thigns%20for%20bots/baby-chick_1f424.png",
                    "goat" : "https://benignking.xyz/thigns%20for%20bots/goat_1f410.png",
                    "horse" : "https://benignking.xyz/thigns%20for%20bots/horse.png",
                    "mouse" : "https://benignking.xyz/thigns%20for%20bots/mouse_1f401.png"
                    }
                #send embed
                embed=discord.Embed(title="🥇 {} 🥇".format(winner), description="Winners collect your ${}".format(str(amount)), color=0xf1c40f)
                embed.set_author(name="THE WINNER IS")
                embed.set_thumbnail(url= icons[winner])
                embed.set_footer(text="🌎 BenignKing.xyz - Paypal.me/B9king - Patreon.com/B9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")
                await raceEmbed.edit(embed=embed)                
        #if their bet isn't a number
        else:
            ##print(amount)
            await message.channel.send("YOUR BET NEEDS TO BE A NUMBER, THIS WILL BE REPLACED WITH AN EMBED SOON")




#----------------------------------------------------------------------------------------------------
#--------------------------LOTTO TICKETS AND SHIT----------------------------------------------------
#----------------------------------------------------------------------------------------------------

    elif message.content == "~scratch $10":
        ID = message.author.id
        
        #get card
        results = twoToOneCard()
        #['LOSER', ['||🍢||', '||🍊||', '||🍨||', '||🍧||', '||🍗||', '||🍨||', '||🍜||', '||🍦||', '||🍾||']]
        
        ##print(results[1])
        
        #handle winning and losing
        if results[0] == "LOSER":
            removeMoney(ID,10)
        else:
            addMoney(ID,10)
        
        #format card
        card = "{}{}{}\n".format(results[1][0],results[1][1],results[1][2])
        card += "{}{}{}\n".format(results[1][3],results[1][4],results[1][5])
        card += "{}{}{}".format(results[1][6],results[1][7],results[1][8])
        
        embed=discord.Embed(title=card, color=0xF79F1F)
        embed.set_author(name="Here's your $10 scratch-off ticket. Match 3 symbols to win".format(message.guild.name))
        embed.set_footer(text="🌎 BenignKing.xyz - Paypal.me/B9king - Patreon.com/B9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")
        await message.channel.send(embed=embed)


    elif message.content == "~scratch $50":
        ID = message.author.id
        
        #get card
        results = threeToOneCard()
        #['LOSER', ['||🍢||', '||🍊||', '||🍨||', '||🍧||', '||🍗||', '||🍨||', '||🍜||', '||🍦||', '||🍾||']]
        
        ##print(results[1])
        
        #handle winning and losing
        if results[0] == "LOSER":
            removeMoney(ID,50)
        else:
            addMoney(ID,100)
        
        #format card
        card = "{}{}{}{}{}\n".format(results[1][0],results[1][1],results[1][2],results[1][3],results[1][4])
        card += "{}{}{}{}{}\n".format(results[1][5],results[1][6],results[1][7],results[1][8],results[1][9])
        card += "{}{}{}{}{}\n".format(results[1][10],results[1][11],results[1][12],results[1][13],results[1][14])
        card += "{}{}{}{}{}\n".format(results[1][15],results[1][16],results[1][17],results[1][18],results[1][19])
        card += "{}{}{}{}{}".format(results[1][20],results[1][21],results[1][22],results[1][23],results[1][24])
        
        embed=discord.Embed(title=card, color=0xF79F1F)
        embed.set_author(name="Here's your $50 scratch-off ticket. Match 5 symbols to win".format(message.guild.name))
        embed.set_footer(text="🌎 BenignKing.xyz - Paypal.me/B9king - Patreon.com/B9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")
        await message.channel.send(embed=embed)
        

    elif message.content.startswith("~lotto"):
        ID = message.author.id
        

        toSend = message.content.replace("~lotto ","")
        toSend = toSend.split(" ")
        for i in range(len(toSend)):
            toSend[i] = int(toSend[i])
        g = lottery(toSend)
        
        removeMoney(ID, 5)
        addMoney(ID, int(g[0]))
        
        win = " ".join(str(x) for x in g[2])
        your = " ".join(str(x) for x in g[1])
        
        ##print(win)
        
               
        embed=discord.Embed(title="Your numbers {} \n Winning numbers {}".format(your,win), color=0xF79F1F)
        embed.set_author(name="Thanks for playing the lotto, you won ${:,}".format(g[0]))
        embed.set_footer(text="🌎 BenignKing.xyz - Paypal.me/B9king - Patreon.com/B9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")
        await message.channel.send(embed=embed)
            
        #except:
            #await message.channel.send("THOSE AREN'T NUMBERS")
            

            
#=========================================================================================================
#=========================================================================================================
#                                 Careers and Education
#=========================================================================================================
#=========================================================================================================

#----------------------------------------------------------------------------------------------------
#--------------------------JOIN THE EDUCATION DLC----------------------------------------------------
#----------------------------------------------------------------------------------------------------
    elif message.content == "~work and education":
        #Get Variables
        ID = message.author.id
        #GET BALANCE
        g = joinWorkAndEducation(ID)
        if g == "PLEASE RUN '~ADD ME' FIRST":
            embed=discord.Embed(title="🎨 I can't seem to find you in the system.", color=0xc0392b, description = "I look forward to having you in the college and watching you succeed, but first you need to type '~add me' to join our little game.")
            embed.set_author(name="Thanks for your interest in the Work and Education Expansion!".format(message.guild.name))
            embed.set_thumbnail(url="https://benignking.xyz/thigns%20for%20bots/default.png")    
            await message.channel.send(embed=embed)  
        elif g == "You're already in here":
            embed=discord.Embed(title="🖼️ It seems you're already in my roster for students!", color=0xc0392b, description = "Feel free to join us for classes or explor your options for employment!")
            embed.set_author(name="Thanks for your interest in the Work and Education Expansion!".format(message.guild.name))
            embed.set_thumbnail(url="https://benignking.xyz/thigns%20for%20bots/default.png")   
            await message.channel.send(embed=embed)  
        else:
            embed=discord.Embed(title="🖌 I look forward to painting memories with you️ and watching you succeed in whatever you choose.".format(str(g)), color=0x27ae60, description = "THIS SECTION WILL EVENTUALLY CONTAIN COMMANDS")
            embed.set_author(name="Welcome To The Education and Work Expansion".format(message.guild.name))
            embed.set_thumbnail(url="https://benignking.xyz/thigns%20for%20bots/default.png")
            await message.channel.send(embed=embed)   

#----------------------------------------------------------------------------------------------------
#--------------------------SEE YOUR OPTIONS FOR COLLEGE----------------------------------------------
#----------------------------------------------------------------------------------------------------
    elif message.content == "~college options":
        #Get Variables
        ID = message.author.id
        #GET BALANCE
        g = checkCollegeOptions(ID)
        if g == "YOU HAVEN'T AGREED TO THE DLC" :
            embed=discord.Embed(title="🎨 I can't seem to find you in the system.", color=0xc0392b, description = "I look forward to having you in the college and watching you succeed, but first you need to type '~work and education' to join our little game.")
            embed.set_author(name="Thanks for your interest in the Work and Education Expansion!".format(message.guild.name))
            embed.set_thumbnail(url="https://benignking.xyz/thigns%20for%20bots/default.png")    
            await message.channel.send(embed=embed)  
        elif g == "YOU'VE BEEN TO COLLEGE":
            embed=discord.Embed(title="🖼️ It seems you've already graduated.", color=0xc0392b, description = "First off **CONGRATS**, I'm so glad to have had you as one of my students. While I enjoyed you being in my classes, it's time for you to get a job out in the real world!")
            embed.set_author(name="Thanks for your interest in the Work and Education Expansion!".format(message.guild.name))
            embed.set_thumbnail(url="https://benignking.xyz/thigns%20for%20bots/default.png")   
            await message.channel.send(embed=embed)  
        else:
            embed=discord.Embed(title="It's going to cost $40,000 to attend, and here's your options to pay that.".format(str(g)), color=0x27ae60)
            embed.set_author(name="Hey {}, thanks for your interest in {} university".format(message.author.name,message.guild.name))
            embed.set_thumbnail(url="https://benignking.xyz/thigns%20for%20bots/default.png")
             
            for i in g:
                embed.add_field(name="{}".format(i[:i.index(",")+1]), value="{}".format(i[i.index(",")+1:]), inline=False) 
            
            await message.channel.send(embed=embed)   



#----------------------------------------------------------------------------------------------------
#-----------------------SEE YOUR OPTIONS FOR EMPLOYMENT----------------------------------------------
#----------------------------------------------------------------------------------------------------
    elif message.content == "~job options":
        #Get Variables
        ID = message.author.id
        #GET BALANCE
        g = availableJobs(ID)
        if g == "YOU HAVEN'T AGREED TO THE DLC" :
            embed=discord.Embed(title="🎨 I can't seem to find you in the system.", color=0xc0392b, description = "I look forward to having you in the college and watching you succeed, but first you need to type '~work and education' to join our little game.")
            embed.set_author(name="Thanks for your interest in the Work and Education Expansion!".format(message.guild.name))
            embed.set_thumbnail(url="https://benignking.xyz/thigns%20for%20bots/default.png")    
            await message.channel.send(embed=embed)  
        else:
            embed=discord.Embed(title="**The Commands are with the Jobs**".format(str(g)), color=0x27ae60)
            embed.set_author(name="Hey {}, here are a list of jobs available for you!".format(message.author.name,message.guild.name))
            embed.set_thumbnail(url="https://benignking.xyz/thigns%20for%20bots/default.png")
             
            for i in g.keys():
                name = i 
                salary = g[i]["salary"]
                field = g[i]["Field"]
                college = g[i]["college"]
                
                #set message for college
                if college:
                    collegeMessage = "✅ college"
                else:
                    collegeMessage = "❌ college"
                
                #salary formatting
                salaryMessage = "{:,}".format(salary)
                
                
                #command maker
                if field == "misc":
                    command = "~Apply misc {}".format(name)
                else:
                    command = "~Apply {}".format(field)
                
                
                
                embed.add_field(name="{}".format(command), value="**Title: {}** - Field: {}, Salary: ${}, {}".format(name,field,salary,collegeMessage), inline=False) 
            
            await message.channel.send(embed=embed)          

#----------------------------------------------------------------------------------------------------
#-----------------------JOIN THE EDUCATION DLC-------------------------------------------------------
#----------------------------------------------------------------------------------------------------
    elif message.content == "~work and education":
        #Get Variables
        ID = message.author.id
        #GET BALANCE
        g = joinWorkAndEducation(ID)
        if g == "PLEASE RUN '~ADD ME' FIRST":
            embed=discord.Embed(title="🎨 I can't seem to find you in the system.", color=0xc0392b, description = "I look forward to having you in the college and watching you succeed, but first you need to type '~add me' to join our little game.")
            embed.set_author(name="Thanks for your interest in the Work and Education Expansion!".format(message.guild.name))
            embed.set_thumbnail(url="https://benignking.xyz/thigns%20for%20bots/default.png")    
            await message.channel.send(embed=embed)  
        elif g == "You're already in here":
            embed=discord.Embed(title="🖼️ It seems you're already in my roster for students!", color=0xc0392b, description = "Feel free to join us for classes or explor your options for employment!")
            embed.set_author(name="Thanks for your interest in the Work and Education Expansion!".format(message.guild.name))
            embed.set_thumbnail(url="https://benignking.xyz/thigns%20for%20bots/default.png")   
            await message.channel.send(embed=embed)  
        else:
            embed=discord.Embed(title="🖌 I look forward to painting memories with you️ and watching you succeed in whatever you choose.".format(str(g)), color=0x27ae60, description = "THIS SECTION WILL EVENTUALLY CONTAIN COMMANDS")
            embed.set_author(name="Welcome To The Education and Work Expansion".format(message.guild.name))
            embed.set_thumbnail(url="https://benignking.xyz/thigns%20for%20bots/default.png")
            await message.channel.send(embed=embed)   

#----------------------------------------------------------------------------------------------------
#-----------------------SEE YOUR OPTIONS FOR EMPLOYMENT----------------------------------------------
#----------------------------------------------------------------------------------------------------
    elif message.content == "~college options":
        #Get Variables
        ID = message.author.id
        #GET BALANCE
        g = checkCollegeOptions(ID)
        if g == "YOU HAVEN'T AGREED TO THE DLC" :
            embed=discord.Embed(title="🎨 I can't seem to find you in the system.", color=0xc0392b, description = "I look forward to having you in the college and watching you succeed, but first you need to type '~work and education' to join our little game.")
            embed.set_author(name="Thanks for your interest in the Work and Education Expansion!".format(message.guild.name))
            embed.set_thumbnail(url="https://benignking.xyz/thigns%20for%20bots/default.png")    
            await message.channel.send(embed=embed)  
        else:
            embed=discord.Embed(title="**The Commands are with the Jobs**".format(str(g)), color=0x27ae60)
            embed.set_author(name="Hey {}, here are a list of jobs available for you!".format(message.author.name,message.guild.name))
            embed.set_thumbnail(url="https://benignking.xyz/thigns%20for%20bots/default.png")
             
            for i in g:                
                embed.add_field(name="{}".format(command), value="**Title: {}** - Field: {}, Salary: ${}, {}".format(name,field,salary,collegeMessage), inline=False) 
            
            await message.channel.send(embed=embed)   


























client.run('NjY1MjA4ODQyODYyNDYwOTYz.XhiSkw.LBWZgFHM9S3sBYIypOs6WGUV9Fo') 

