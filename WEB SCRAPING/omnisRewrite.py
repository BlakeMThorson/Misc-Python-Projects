#TO DO LIST
# 1) add the satire function using getSatire()







#======================================== MASS IMPORT STATEMENTS
import discord
from discord.ext import commands
import random
import asyncio
client=discord.Client()

#OLD BOTS
from asd import *
from MOVIEHELPER import *
import wikipedia
from pokedex import *

#new bots
import markovify
from makeAscii import *
from contentagrigator import *
from swearingManager import *

#helper shit
from omnisHelper import *
#======================================== END MASS IMPORT STATEMENTS


#======================================== START UP SHIT FOR BOT
client = commands.Bot(command_prefix='~')
#normal bot
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("benignking.xyz/omnis.html"))
    print("Ready!")


#======================================== END START UP SHIT


#======================================================================================================================================= COMMANDS

#----------------------------------------------------------------------------------------------------------------------------------------------------> UTILITY
@client.command()
async def responseTime(ctx):
    await ctx.send( "I currently have a response time of {} MS".format(round(client.latency * 1000) ))
    

    
    

@client.event
async def on_member_join(member):
    guild = member.guild
    greeting = """Please welcome {0.mention} to {1.name}!
I've DM'd you the help commands for the bots on server. Please introduce yourself and make yourself at home.
""".format(member,guild)
    dm = """Welcome to the server, my commands can be found on BenignKing.xyz/Omnis. If you have questions feel free to DM my creator. 
    
    Server rules:
         - don't be a cunt without reason
         - don't be an annoyance
         - this is secret, it doesn't exist, and whatever happens stays here
         
    To get a role:
         - we give everyone 24 hours to ensure that nothing untoward will happen shortly after them joining, after which you will recieve your relevant roles
         - this can be mitigated if an established member vouches for you
    
    
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

    await member.send(dm)
    await x.send(greeting) 





    
#----------------------------------------------------------------------------------------------------------------------------------------------------> FOOD / DRINK 

@client.command()
async def taco( ctx ):
    x = Taco()
    taco = "{}".format(x["recipe"])
    embed=discord.Embed(title= "Ceasar's Hottest Tacos: " , color=0xfce21b, description = taco , url = x["url"])
    embed.set_thumbnail(url="https://files.catbox.moe/prc9ze.gif")
    embed.set_footer(text="b9king#6857 ; BenignKing.xyz ; Patreon.com/b9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")
    await ctx.send(embed=embed) 

@client.command(aliases = ["drink"])
async def makeDrink( ctx, ingredient ):
    try:
        x = ingredientSearch(ingredient)
        embed=discord.Embed(title= x["ingredients"] , color=0x746A69, description = x["recipe"])
        embed.set_author(name= x["name"])
        embed.set_thumbnail(url=x["image"])
        embed.set_footer(text="Made by b9king#6857: benignking.xyz: patreon.com/b9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")     
        await ctx.send(embed=embed)        
    except:
        await ctx.send("COULDN'T FIND THAT INGREDIENT")    





#---------------------------------------------------------------------------------------------------------------------------------------------------->  FUN / FACTS


@client.command()
async def steamGame( ctx, url ):
    g = steamGameInfo( url )
    await ctx.send( embed = g )


@client.command()
async def weather( ctx , zipcode, country):
    g = getWeather( zipcode, country )
    await ctx.send( embed = g )
@client.command()
async def rhyme(ctx , word):
    embed=discord.Embed(title="**Rhymes for {}**".format(word), description = getRhymes(word)[:1000] ,color=0x00b894)
    embed.set_footer(text="Made by b9king#6857: benignking.xyz: patreon.com/b9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")        
    await ctx.send( embed = embed)    

@client.command()
async def bibleSearch( ctx, term ):

    ass = bibleSearchas( term )
    
    if len(ass) >= 10:
        ass = ass[:10]
    
    embed=discord.Embed(title="**Results in the KJV Bible for '{}'**".format(term.title()), color=0x00b894)
    
    for i in ass:
        embed.add_field(name= i[0], value= i[1], inline=False)
    embed.set_footer(text="Made by b9king#6857: benignking.xyz: patreon.com/b9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")        
     
    await ctx.send( embed = embed)

@client.command()
async def anime( ctx, url):
    print(url)
    g = animeID( url ) 
    await ctx.send( embed = g )

@client.command()
async def cat( ctx ):
    embed=discord.Embed(title= catFacts() , color=0x746A69)
    embed.set_author(name="CAT FACT:")
    embed.set_thumbnail(url="https://i.pinimg.com/originals/dc/d7/03/dcd70309b118dfbcce7689886fae9a38.gif")
    embed.set_footer(text="Made by b9king#6857: benignking.xyz: patreon.com/b9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")     
    await ctx.send(embed=embed)
    
@client.command()
async def wiki( ctx , article):
    g = wikipedia.page(article)
    embed=discord.Embed(title= g.title, color=0x746A69, url = g.url, description = g.content[:500]+"...")
    embed.set_thumbnail(url="https://ciapannaphoto.files.wordpress.com/2012/06/p1040091_statue_manual1000px.jpg")
    embed.set_footer(text="Made by b9king#6857: benignking.xyz: patreon.com/b9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")     
    await ctx.send(embed=embed)

@client.command()
async def wikiHow( ctx ):
    try:
        country = getWinner()
        embed=discord.Embed(title= country[0], color=0xff0000, description = country[1][:250] + "...")
        embed.set_thumbnail(url= country[2])
        embed.set_footer(text="Made by b9king#6857: benignking.xyz: patreon.com/b9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")        
        await ctx.send(embed=embed)        
    except:
        country = getWinner()
        embed=discord.Embed(title= country[0], color=0xff0000, description = country[1][:250] + "...")
        embed.set_thumbnail(url= country[2])
        embed.set_footer(text="Made by b9king#6857: benignking.xyz: patreon.com/b9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")        
        await ctx.send(embed=embed)     
        
@client.command()
async def idea( ctx ):
    embed=discord.Embed(title= startUp() , color=0x7BAA47)
    embed.set_author(name="I GOT AN IDEA")
    embed.set_thumbnail(url="https://static.thenounproject.com/png/247517-200.png")
    await ctx.send(embed=embed)        

@client.command(aliases = ["8ball"])
async def _8ball( ctx, question):
    eightball = ["it is certain", "it is decidedly so", "without a doubt", "yes-definitely", "you may rely on it", "as I see it, yes","most likely","outlook good","yes","signs point to yes", "reply hazy, try again", "ask again later", "better not tell you now","cannot predict now","concentrate and ask again", "Don't count on it", "My reply is no","my sources say no", "Outlook not so good", "very doubtful"]
    msg = " 🎱 In regards to '" + question + "', " + random.choice(eightball) + "."
    await ctx.send( msg )

@client.command(aliases = ["holidays","getHolidays"])
async def holiday( ctx ):
    unformattedHolidays = getClosestHolidays()
    formatted = holidayFormatter(unformattedHolidays)
    await ctx.send(embed = formatted)
    
@client.command()
async def cute( ctx ):
    await ctx.send( embed = getCuteAnimal() )


    

#----------------------------------------------------------------------------------------------------------------------------------------------------> Health / PSAs

@client.command()
async def country( ctx ):
    
    country = ctx.message.content
    country = country.replace("~country ","")
    country = cCountry(country)
    
    embed=discord.Embed(title="**Corona Information For {}:**".format(country["country"]), color=0xff0000)
    embed.set_thumbnail(url= country["countryInfo"]["flag"])
    embed.add_field(name="Cases:", value="{:,}".format(int(country["cases"])), inline=True)
    embed.add_field(name="New Cases Today", value="{:,}".format(int(country["todayCases"])), inline=True)
    embed.add_field(name="Deaths", value="{:,}".format(int(country["deaths"])), inline=True)
    embed.add_field(name="Deaths Today", value="{:,}".format(int(country["todayDeaths"])), inline=True)
    embed.add_field(name="Recovered", value="{:,}".format(int(country["recovered"])), inline=True)
    embed.add_field(name="Cases Per Million", value="{:,}".format(int(country["casesPerOneMillion"])), inline=True)
    #embed.add_field(name="Deaths Per Million", str(country["deathsPerOneMillion"]), inline=True)
    embed.set_footer(text="Made by b9king#6857: benignking.xyz: patreon.com/b9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")        
    await ctx.send(embed=embed)        

@client.command()
async def state( ctx, state):
    
    state = ctx.message.content
    state = state.replace("~state ","")    
    
    
    try:
        abbreviation = {'Alaska': 'AK', 'Alabama': 'AL', 'Arkansas': 'AR', 'American Samoa': 'AS', 'Arizona': 'AZ', 'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT', 'District of Columbia': 'DC', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA', 'Guam': 'GU', 'Hawaii': 'HI', 'Iowa': 'IA', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Massachusetts': 'MA', 'Maryland': 'MD', 'Maine': 'ME', 'Michigan': 'MI', 'Minnesota': 'MN', 'Missouri': 'MO', 'Northern Mariana Islands': 'MP', 'Mississippi': 'MS', 'Montana': 'MT', 'National': 'NA', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Nebraska': 'NE', 'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'Nevada': 'NV', 'New York': 'NY', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Puerto Rico': 'PR', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Virginia': 'VA', 'Virgin Islands': 'VI', 'Vermont': 'VT', 'Washington': 'WA', 'Wisconsin': 'WI', 'West Virginia': 'WV', 'Wyoming': 'WY'}
        country = cState(state)
        embed=discord.Embed(title="**Corona Information For {}:**".format(country["state"]), color=0xff0000)
        embed.set_thumbnail(url= "https://www.50states.com/images/redesign/flags/{}-largeflag.png".format(  abbreviation[state.title()].lower() ))
        embed.add_field(name="Cases:", value="{:,}".format(int(country["cases"])), inline=True)
        embed.add_field(name="New Cases Today", value="{:,}".format(int(country["todayCases"])), inline=True)
        embed.add_field(name="Deaths", value="{:,}".format(int(country["deaths"])), inline=True)
        embed.set_footer(text="Made by b9king#6857: benignking.xyz: patreon.com/b9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")        
        await ctx.send(embed=embed)
    except:
        message = "the fuck kinda state is {}?".format(state)
        await ctx.send(message)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#{'Date calculated': 'The data below reflects new cases since Sept. 9, 2020.', 'Total infected students': '1,732', 'Today infected students': '111', 'Total infected employees': '23', 'Today infected employees': '2', 'Percent Students': '5.77%', 'Percent Employees': '0.08%'}


@client.command()
async def Uiowa( ctx ):
    stats = getIowaCovid()

    embed=discord.Embed(title="Uiowa Corona Information", description = stats['Date calculated'], color=0xffdd4d)
    embed.set_thumbnail(url= "https://coronavirus.uiowa.edu/sites/coronavirus.uiowa.edu/files/2020-06/COVID-19-Building%20Signage%402x.png")
    
    embed.add_field(name="New Student Cases Today", value= stats["Today infected students"] , inline=True)
    embed.add_field(name="Total Student Cases", value= stats["Total infected students"] , inline=True)
    embed.add_field(name="Percentage Of Students Infected", value= stats["Percent Students"] , inline=True)
    embed.add_field(name="New Employee Cases Today", value= stats["Today infected employees"] , inline=True)
    embed.add_field(name="Total Employee Cases", value= stats["Total infected employees"] , inline=True)
    embed.add_field(name="Percentage Of Employees Infected", value= stats["Percent Employees"] , inline=True)    
    
    embed.set_footer(text="Made by b9king#6857: benignking.xyz: patreon.com/b9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")        
    await ctx.send(embed=embed)   


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

@client.command()
async def corona( ctx ) :
    country = cGet()
    
    embed=discord.Embed(title="**GENERAL INFORMATION ABOUT CORONA**", color=0xff0000)
    embed.set_thumbnail(url= "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/facebook/65/face-with-medical-mask_1f637.png")
    embed.add_field(name="Cases:", value="{:,}".format(country["cases"]), inline=True)
    embed.add_field(name="Deaths:", value="{:,}".format(country["deaths"]), inline=True)
    embed.add_field(name="Recovered:", value="{:,}".format(country["recovered"]), inline=True)
    embed.set_footer(text="Made by b9king#6857: benignking.xyz: patreon.com/b9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")        
    await ctx.send(embed=embed)     


#----------------------------------------------------------------------------------------------------------------------------------------------------> Misc


#----------------------------------------------------------------------------------------------------------------------------------------------------> Movies    

@client.command()
async def search( ctx, movie):
    fuckYou = getByName(movie)
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
    embed.set_footer(text="Made by b9king#6857: benignking.xyz: patreon.com/b9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")     
    await ctx.channel.send(embed=embed)    
    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

@client.command()
async def genres(ctx):
    genres = ['<:action:643387530170990610> Action', '<:adult:643387530586357760> Adult', '<:adventure:643387530582032384> Adventure', '<:animation:643387530573512714> Animation', '<:biography:643387530351476747> Biography', '<:comedy:643387530523312149> Comedy', '<:crime:643387530594484224> Crime', '<:documentary:643387530691215360> Documentary', '<:drama:643387530594615336> Drama', '<:family2:643387530255007756> Family', '<:fantasy:643387530229579778> Fantasy', '<:filmnoir:643387530678370304> Film-Noir', '<:history:643387530640752660> History', '<:horror:643387530716250112> Horror', '<:music:643387530691084318> Music', '<:music:643387530691084318> Musical', '<:mystery:643387530682564609> Mystery', '<:news:643387530707730441> News', '<:realitytv:643387530838016001> Reality-TV', '<:romance:643387530699603978> Romance', '<:scifi:643387531085217802> Sci-Fi', '<:short:643387530359865345> Short', '<:sport:643387530724638750> Sport', '<:thriller:643387530909188116> Thriller', '<:war:643387530942742539> War', '<:western:643387530531700748> Western']
    embed=discord.Embed()
    embed.add_field(name="Here are all of the genres in the bot's database!",value = "use ~get (GENRE) to get a random movie", inline=False)
    embed.set_footer(text="Made by b9king#6857: benignking.xyz: patreon.com/b9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")     
    for i in genres:
        i = i.split()
        embed.add_field(name= i[0] + " " + i[1], value="~get {}".format(  i[1]  ), inline=True)
    await ctx.send(embed=embed)       
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

@client.command()
async def get( ctx, genre):
    fuck = getMovie( genre ) 
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
    embed.set_footer(text="Made by b9king#6857: benignking.xyz: patreon.com/b9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")     
    await ctx.send(embed=embed)       


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

@client.command()
async def randomMovie(ctx):
    fuck = trueRandom()
    image = fuck["poster_400x570"]
    fuckYou = getByID(fuck["imdb"])
    z = fuckYou[0]
    stars = fuckYou[1]
    dumpt = formatter(z.get('genre'))
    genre = ""
    for i in dumpt:
        genre += i + "\n"
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
    embed.set_footer(text="Made by b9king#6857: benignking.xyz: patreon.com/b9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")     
    await ctx.channel.send(embed=embed)              

#----------------------------------------------------------------------------------------------------------------------------------------------------> OTHER BOTS


#----------------------------------------------------------------------------------------------------------------------------------------------------> NLP / TEXT GEN

@client.command()
async def cards( ctx ):
    thePickle = pickle.load( open( "cardsAgainstHumanity.pickle", "rb" ) )
    reconstituted_model = markovify.Text.from_json(thePickle)
    cards = ""
    count = 0
    while count != 10:
        x = reconstituted_model.make_sentence()
        if x != None:
            cards += "{} ) {} \n".format(count+1,x)  
            count += 1
    embed=discord.Embed(title= "Markov Against Humanity", color=0x746A69, description = "The following cards were generated using a Markov Chain :tm: (state size = 2)")
    embed.add_field(name= "First Set", value= cards)
    embed.set_thumbnail(url="https://files.catbox.moe/6bywsr.jpg")  
    embed.set_footer(text="Made by b9king#6857: benignking.xyz: patreon.com/b9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")     
    await ctx.send(embed=embed)    
    

@client.command()
async def fortune( ctx ):
    thePickle = pickle.load( open( "fortuneCookies.pickle", "rb" ) )
    reconstituted_model = markovify.Text.from_json(thePickle)
    cards = ""
    count = 0
    while count != 10:
        x = reconstituted_model.make_sentence()
        if x != None:
            cards += "{} ) {} \n".format(count+1,x)  
            count += 1
    embed=discord.Embed(title= "Markov Cookie", color=0x746A69, description = "The following fortunes were generated using a Markov Chain :tm: (state size = 2)")
    embed.add_field(name= "First Set", value= cards)
    embed.set_thumbnail(url="https://i.pinimg.com/236x/87/f5/f7/87f5f7b8039c88f2f2c6e269dda50b75.jpg")  
    embed.set_footer(text="Made by b9king#6857: benignking.xyz: patreon.com/b9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")     
    await ctx.send(embed=embed)       


@client.command()
async def conspiracy( ctx ):
    thePickle = pickle.load( open( "conspiracies.pickle", "rb" ) )
    reconstituted_model = markovify.Text.from_json(thePickle)
    cards = ""
    count = 0
    while count != 5:
        x = reconstituted_model.make_sentence()
        if x != None:
            cards += "{} ) {} \n".format(count+1,x)  
            count += 1
    embed=discord.Embed(title= "Markov-conspiracies", color=0x746A69, description = "The following conspiracies were generated using a Markov Chain :tm: (state size = 3 : there will be a lot of repeats but this makes it more coherent.)")
    embed.add_field(name= "First Set", value= cards)
    embed.set_thumbnail(url="https://cdn.vox-cdn.com/thumbor/MnXj3KNjD9rw7j8OObK-cBXzBQk=/230x145:1575x1154/1200x800/filters:focal(230x145:1575x1154)/cdn.vox-cdn.com/uploads/chorus_image/image/45894920/deathofcaesar.0.0.jpg")  
    embed.set_footer(text="Made by b9king#6857: benignking.xyz: patreon.com/b9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")     
    await ctx.send(embed=embed)         
    
@client.command()
async def florida( ctx ):
    with open('floridaMarkov.pickle', 'rb') as gator:
        markovModel = pickle.load(gator)  
        floridaMarkov = markovify.Text.from_json(markovModel)        
    embed=discord.Embed(title= floridaMarkov.make_sentence(), color=0x720027)
    embed.set_author(name="{} News Update: Florida Man Edition!".format(ctx.guild.name))
    embed.set_thumbnail(url="https://github.com/Former-Addict/Florida-Man-Discord-Bot/blob/master/florida%20man.png?raw=true")
    await ctx.send(embed=embed)       
    

@client.command()
async def ascii( ctx , inverted , url ):
    if inverted == "true" or inverted == "True":
        inverted = True
    else:
        inverted = False
    try:
        toSend = makeForDiscord( url , inverted )
    except:
        toSend = "Hey, right now I don't support PNGs, and certain sites REALLY don't like bots accessing their shit. This will be fixed soon, in the meantime you can upload your jpg to discord and link me it!"
    await ctx.send(toSend)    





#======================================================================================================================================= COMMANDS END

@client.command()
async def getTop(ctx, word):
    word = word.lower()
    people = getTop1(word)
    people = people[-3:]
    for i in range( len(people) ):
        user =  client.get_user(people[i][0])
        people[i][0] = user.name
    print(people)
    embed=discord.Embed(title= "The Most Heavy Users Of {}".format(word), color=0x00b894, description = "the following users have used {} more than anyone else I am forced to monitor, congrats on overusing google's banned words!".format(word).title())
    
    embed.add_field(name= "First", value= people[-1][0])
    embed.add_field(name= "Second", value= people[-2][0])
    embed.add_field(name= "Third", value= people[-3][0])
    
    embed.set_thumbnail(url="https://static.thenounproject.com/png/1121441-200.png")  
    embed.set_footer(text="Made by b9king#6857: benignking.xyz: patreon.com/b9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")     
    await ctx.send(embed=embed)        




    
client.run('NjcyMzE4MDk0MjM1OTI2NTI4.XjJwhA.sTlk4bSNcNOkbbEH23yBQLl4h_U')