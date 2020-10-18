import discord
import random
import asyncio
client=discord.Client()

#OLD BOTS
from asd import *
from MOVIEHELPER import *
from weatherHelper import *
client=discord.Client()

@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')
    
    

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
        await client.change_presence(status=discord.Status.online, activity=discord.Game("Made By B9king"))
        
    @client.event
    async def on_message(message):
        message.content = message.content.lower()
        
    #=========================================================================================================
    #=========================================================================================================
    #                                       OTHER BOTS
    #=========================================================================================================
    #=========================================================================================================
       
       #---------------------------------------------------------------------------------------------------- 
        if message.content.startswith("~idea"):
            embed=discord.Embed(title= startUp() , color=0x7BAA47)
            embed.set_author(name="HOLY FUCK DUDE I GOT AN IDEA")
            embed.set_thumbnail(url="https://media.tenor.com/images/a32b1c862f8ffb730ba22fda8076c82c/tenor.gif")
            embed.set_footer(text="🌎 BenignKing.xyz - Paypal.me/B9king - Patreon.com/B9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")
            await message.channel.send(embed=embed)
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
    



client.run('NjcyMzE4MDk0MjM1OTI2NTI4.XjJwhA.sTlk4bSNcNOkbbEH23yBQLl4h_U')