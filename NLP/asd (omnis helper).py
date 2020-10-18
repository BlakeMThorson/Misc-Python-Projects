from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Soup
import random
import json
import fuckyou
from fuckyou import *
import re
import pickle
import urllib.request 
from datetime import date
import datetime
import urllib.request 
import discord
import asyncio
import calendar

#import code
#removes special characters
#x = ''.join([i if ord(i) < 128 else ' ' for i in toReturn])


#SHIT FOR PICKLE
#with open('entitledStory.pickle', 'wb') as handle:
    #pickle.dump(toReturn, handle, protocol=pickle.HIGHEST_PROTOCOL)       
#with open('entitledStory.pickle', 'rb') as handle:
    #toReturn = pickle.load(handle)

def tes123t(url):    
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('utf-8')
    page_soup = Soup(data, "html.parser") 
    rating = page_soup.findAll("div", {"class" : "summary column"})
    return rating[0].text.replace("\n","").replace("\t","").replace("\r","")
    
    
def steamGameInfo( url1 = "https://store.steampowered.com/app/22120/Penumbra_Black_Plague_Gold_Edition/" ) :
    #save a copy of the URL
    url2 = url1
    
    #use url1 to get the ID
    firstSlash = url1.index("app/")+4
    url1 = url1[firstSlash:]
    firstSlash = url1.index("/")
    url1 = url1[:firstSlash]
    
    #get the lowest prices
    url = "https://www.cheapshark.com/api/1.0/games?steamAppID={}".format(url1)
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    cheapShark = json.loads(infile)   
        
    #get the general information
    url = "https://store.steampowered.com/api/appdetails?appids={}".format(url1)
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    steam = json.loads(infile)
    
    genres = ""
    for i in steam[url1]["data"]["genres"]:
        genres+= i["description"] + " "
    
    
    gameStats = {
        "name" : cheapShark[0]["external"],
        "cheapest" : cheapShark[0]["cheapest"],
        "short desc" : steam[url1]["data"]["short_description"],
        "image" : steam[url1]["data"]["header_image"],
        "current price" : steam[url1]["data"]["price_overview"]["final_formatted"],
        "genres" : genres,
        "rating" : tes123t( url2 )
        }
    
    
    embed=discord.Embed(title= "Information for {}".format(gameStats["name"]) , color=0x00b894, description = "current price {}, lowest price ${}".format(gameStats["current price"],gameStats["cheapest"]) , url = url2)
    embed.set_thumbnail(url= gameStats["image"])
    #short description
    embed.add_field(name= "Description of Game", value= gameStats["short desc"], inline=True)
    #genres
    embed.add_field(name= "Genres", value= gameStats["genres"] , inline=True)
    #rating
    embed.add_field(name= "Rating", value= gameStats["rating"] , inline=True)
    
    embed.set_footer(text="b9king#6857 ; BenignKing.xyz ; Patreon.com/b9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")    
    
    return embed
    
    
def animeID( url1 ):
    url = "https://trace.moe/api/search?url={}".format(url1)
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    a = json.loads(infile)      
    
    animeInfo = {
        "title" : a["docs"][0]["anime"],
        "title english" : a["docs"][0]["title_english"],
        "season" : a["docs"][0]["season"],
        "episode" : a["docs"][0]["episode"],
        "certainty" : a["docs"][0]["similarity"],
        "adult" : a["docs"][0]["is_adult"]
        }
    
    embed=discord.Embed(title= "This image comes from {} / {}".format(  animeInfo["title"],animeInfo["title english"]  ) , color=0x00b894, description = "I have a {}% certainty".format(  round(animeInfo["certainty"]*100,2) ) )
    embed.set_thumbnail(url = url1)    
     
    #season / episode
    embed.add_field(name= "Season / Episode", value= "Season : {} , Episode : {}".format(  animeInfo["season"],animeInfo["episode"]  ) , inline=True)
    #is it hentia
    embed.add_field(name= "Is It A Hentai?", value= animeInfo["adult"] , inline=True)
    
    
    embed.set_footer(text="b9king#6857 ; BenignKing.xyz ; Patreon.com/b9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")

    return embed

    
def getWeather( zipcode, country ):
    #do less checks
    country = country.lower()
    if country.upper() in ['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AN', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BM', 'BN', 'BO', 'BR', 'BS', 'BT', 'BU', 'BV', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CS', 'CU', 'CV', 'CX', 'CY', 'CZ', 'DD', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'FX', 'GA', 'GB', 'GD', 'GE', 'GF', 'GH', 'GI', 'GL', 'GM', 'GN', 'GP', 'GQ', 'GR', 'GS', 'GT', 'GU', 'GW', 'GY', 'HK', 'HM', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'MG', 'MH', 'ML', 'MN', 'MM', 'MO', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NF', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NT', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'ST', 'SU', 'SV', 'SY', 'SZ', 'TC', 'TD', 'TF', 'TG', 'TH', 'TJ', 'TK', 'TM', 'TN', 'TO', 'TP', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'UM', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'YD', 'YE', 'YT', 'YU', 'ZA', 'ZM', 'ZR', 'ZW', 'ZZ']:
        pass
    elif country in ["us", "mcdonalds"]:
        country = "US"
    elif country in ["gb", "britain", "bongland"]:
        country = "GB"
    elif country in ["ca", "canada", "hockey", "maple"]:
        country = "CA"
    else:
        return "the fuck kind of country code is {}".format(country)
    url = "http://api.openweathermap.org/data/2.5/weather?zip={},{}&appid=62f811ebb12f045b43e35fac7ae18b88".format(zipcode, country)
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    a = json.loads(infile)    
    current = {
        "conditions" : { "main": a["weather"][0]["main"], "desc": a["weather"][0]["description"], "icon" : a["weather"][0]["icon"] },
        "name" : a["name"],
        "timezone": a["timezone"],
        "temp" : { "temp" : round( a["main"]["temp"] * 9/5 - 459.67 , 2 )  ,  "feels like" : round(a["main"]["feels_like"] * 9/5 - 459.67 , 2), "temp min" : round(a["main"]["temp_min"] * 9/5 - 459.67,2), "temp max" : round(a["main"]["temp_max"] * 9/5 - 459.67,2) },
        "Humidity" : a["main"]["humidity"]
        }
    embed=discord.Embed(title= "Current Weather For {}".format(current["name"]) , color=0x00b894, description = "It is currently {}F, feels like {}F".format(  current["temp"]["temp"],current["temp"]["feels like"] ) )
    embed.set_thumbnail(url="https://openweathermap.org/img/wn/{}.png".format(current["conditions"]["icon"]))
    #max / min
    embed.add_field(name= "Today's High / Low", value= " {}F / {}F ".format( current["temp"]["temp min"],current["temp"]["temp max"]   ) , inline=True)      
    #current weather conditions
    embed.add_field(name= "Current Condition: {}".format(current["conditions"]["main"]), value= current["conditions"]["desc"] , inline=True)
    #humidity
    embed.add_field(name= "Current Humidity", value= current["Humidity"] , inline=True)    
    embed.set_footer(text="b9king#6857 ; BenignKing.xyz ; Patreon.com/b9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")
    return embed
    
    
def getRhymes( word ):
    url = "https://rhymebrain.com/talk?function=getRhymes&word={}".format(word)
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    a = json.loads(infile)
    toReturn = ""
    for i in a:
        toReturn += i["word"] + "\n"
    return toReturn
    

def bibleSearchas(term):
    term = term.replace(" ","%20")
    term = term.replace("'","%27")
    url = "https://api.biblia.com/v1/bible/search/kjv.txt?query={}&mode=verse&start=0&limit=20&key=fd37d8f28e95d3be8cb4fbc37e15e18e".format(term)
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    a = json.loads(infile)
    
    toReturn = []
    
    for i in a["results"]:
        toReturn.append( [ i["title"],i["preview"] ] )
    return toReturn

    

    
def getCuteAnimal():
    import urllib.request    
    url = "https://gruntle.me/"
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('utf-8')
    page_soup = Soup(data, "html.parser") 
    images = page_soup.findAll("img")
    cuteAnimal = "https://gruntle.me/" + images[0]["src"][1:]
    
    embed=discord.Embed(title="**Enjoy The Cute Animal!**", color=0x00b894)
    embed.set_image(url= cuteAnimal)  
    embed.set_footer(text="Made by b9king#6857: benignking.xyz: patreon.com/b9king", icon_url = "https://files.catbox.moe/4xckm3.PNG") 
    return embed


def holidayFormatter(unformatted):
    today = datetime.date.today()
    embed=discord.Embed(title="**Holidays In The Next Week**", color=0x00b894)
    embed.set_thumbnail(url= "https://media.discordapp.net/attachments/643387353339265026/754628005862834237/unknown.png")
    
    for i in unformatted:
        
        holiName = "{} - {}".format( i["date"]["iso"], i["name"] )
        holiScription = i["description"]
        
        embed.add_field(name= holiName, value= holiScription, inline=True)




    embed.set_footer(text="Made by b9king#6857: benignking.xyz: patreon.com/b9king", icon_url = "https://files.catbox.moe/4xckm3.PNG")        
    
    
    return embed


def getClosestHolidays():
    today = datetime.date.today()
    
    with open('{}sortedHolidays.pickle'.format(today.year), 'rb') as handle:
        toReturn = pickle.load(handle)
        
    currentHolidays = []   
    
    for i in toReturn[str(today.year)][int(today.month)]:
        holiDate = datetime.date( i["date"]["datetime"]["year"], i["date"]["datetime"]["month"], i["date"]["datetime"]["day"])
        daysTil = today - holiDate
        if daysTil.days <= 0 and daysTil.days >= -7:
            currentHolidays.append( i )
        
    return currentHolidays

    
    
    
    
    
    
def getIowaCovid():
    
    stats = {
        "Date calculated" : "",
        "Total infected students" : 0,
        "Today infected students" : 0,
        "Total infected employees" : 0,
        "Today infected employees" : 0,
        "Percent Students" : 0,
        "Percent Employees" : 0
        }
        
    url = "https://coronavirus.uiowa.edu/covid-19-numbers"
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('utf-8')
    page_soup = Soup(data, "html.parser") 
    
    #set the date that it was collected, why the fuck is everything in em tags?
    stats["Date calculated"] = page_soup.findAll("em")[0].text
    
    #get student infected
    numbers = page_soup.findAll("td")
    for i in range( len(numbers) ):
        numbers[i] = int(numbers[i].text.replace(",",""))
    
    stats["Today infected students"] = "{:,}".format(numbers[0])
    stats["Total infected students"] = "{:,}".format(numbers[1])
    stats["Percent Students"] = "{}%".format( round((numbers[1]/30000)*100,2) )
    

    stats["Today infected employees"] = "{:,}".format(numbers[2])
    stats["Total infected employees"] = "{:,}".format(numbers[3])
    stats["Percent Employees"] = "{}%".format( round((numbers[3]/30000)*100,2) ) 
    
    return stats    




cards = {
    'Death' : "https://www.free-tarot-reading.net/img/cards/rider-waite/death.jpg" , 
    'Judgement' : "https://www.free-tarot-reading.net/img/cards/rider-waite/judgement.jpg", 
    'Justice' : "https://www.free-tarot-reading.net/img/cards/rider-waite/justice.jpg" , 
    'Strength': "https://www.free-tarot-reading.net/img/cards/rider-waite/strength.jpg", 
    'Temperance' : "https://www.free-tarot-reading.net/img/cards/rider-waite/temperance.jpg", 
    'The Chariot' : "https://www.free-tarot-reading.net/img/cards/rider-waite/the-chariot.jpg", 
    'The Devil' : "https://www.free-tarot-reading.net/img/cards/rider-waite/the-devil.jpg", 
    'The Emperor' : "https://www.free-tarot-reading.net/img/cards/rider-waite/the-emporer.jpg", 
    'The Empress' :  "https://www.free-tarot-reading.net/img/cards/rider-waite/the-empress.jpg",
    'The Fool': "https://www.free-tarot-reading.net/img/cards/rider-waite/the-fool.jpg", 
    'The Hanged Man': "https://www.free-tarot-reading.net/img/cards/rider-waite/the-hanged-man.jpg", 
    'The Hermit' : "https://www.free-tarot-reading.net/img/cards/rider-waite/the-hermit.jpg" , 
    'The Hierophant': "https://www.free-tarot-reading.net/img/cards/rider-waite/the-heirophant.jpg", 
    'The High Priestess': "https://www.free-tarot-reading.net/img/cards/rider-waite/the-high-priestess.jpg", 
    'The Lovers': "https://www.free-tarot-reading.net/img/cards/rider-waite/the-lovers.jpg", 
    'The Magician': "https://www.free-tarot-reading.net/img/cards/rider-waite/the-magician.jpg", 
    'The Moon': "https://www.free-tarot-reading.net/img/cards/rider-waite/the-moon.jpg", 
    'The Star': "https://www.free-tarot-reading.net/img/cards/rider-waite/the-star.jpg", 
    'The Sun': "https://www.free-tarot-reading.net/img/cards/rider-waite/the-sun.jpg", 
    'The Tower': "https://www.free-tarot-reading.net/img/cards/rider-waite/the-tower.jpg", 
    'The World': "https://www.free-tarot-reading.net/img/cards/rider-waite/the-world.jpg", 
    'Wheel of Fortune': "https://www.free-tarot-reading.net/img/cards/rider-waite/wheel-of-fortune.jpg"
    }




def getReading(section):
    with open('tarot.pickle', 'rb') as handle:
        readings = pickle.load(handle)
    card = random.choice( list(readings[section].keys()) ) 
    reading = random.choice( readings[section][card] ) 
    return [card,cards[card],reading]
    



def getWords():
    import urllib.request    
    url = "https://www.talkenglish.com/vocabulary/top-1500-nouns.aspx"
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('utf-8')
    page_soup = Soup(data, "html.parser") 
    images = page_soup.findAll("a")
    return images


#-------------------GET FLORIDA MAN-----------------------
def getParents(fuck):
    fuck = fuck * 14
    with open('entitledStory.pickle', 'rb') as handle:
        toReturn = pickle.load(handle)
    with open('entitledTitle.pickle', 'rb') as handle:
        toReturnTitle = pickle.load(handle)       
    import urllib.request    
    url = "https://api.pushshift.io/reddit/search/submission/?subreddit=entitledparents&size=1000&after={}d".format(fuck)
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    a = json.loads(infile) 
    for i in a["data"]:
        try:
            if i["selftext"] not in toReturn:
                toReturn += i["selftext"].replace("\n", " ") + "\n"
        except:
            pass
        if i["title"] not in toReturnTitle:
            toReturnTitle += i["title"].replace("\n", " ") + "\n"            

    with open('entitledStory.pickle', 'wb') as handle:
        pickle.dump(toReturn, handle, protocol=pickle.HIGHEST_PROTOCOL)    
    with open('entitledTitle.pickle', 'wb') as handle:
        pickle.dump(toReturnTitle, handle, protocol=pickle.HIGHEST_PROTOCOL)     
    

    print(str(toReturn.count("\n")) + " TOTAL STORIES")
    
    
#____________________________________________________________________________________________________________________________________________________________________________________________________________________________


#-------------------make florida man---------------------
def makeFlorida():
    import markovify
    
    # Get raw text as string.
    with open("florida2.txt") as f:
        text = f.read()
    
    # Build the model.
    text_model = markovify.NewlineText(text)
    
    # Print five randomly-generated sentences
    for i in range(5):
        print(text_model.make_sentence())




#-------------------GET FLORIDA MAN-----------------------
def getFlorida(fuck):
    fuck = fuck * 14
    with open('florida.pickle', 'rb') as handle:
        toReturn = pickle.load(handle)    
    


    import urllib.request    
    url = "https://api.pushshift.io/reddit/search/submission/?subreddit=FloridaMan&size=1000&q=%27florida%20man%27&after={}d".format(fuck)
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    a = json.loads(infile) 
    

        
    try:
        for i in a["data"]:
            if i["title"] not in toReturn:
                toReturn += i["title"] + "\n"
    except:
        print("we failed at j = {}".format(j))
    
    with open('florida.pickle', 'wb') as handle:
        pickle.dump(toReturn, handle, protocol=pickle.HIGHEST_PROTOCOL)        

    print(str(toReturn.count("\n")) + " total headlines")

    
#-------------------VIPER MAKER----------------------------
def getViperAlbum():
    import markovify
    
    # Get raw text as string.
    with open("viperAlbum.txt") as f:
        text = f.read()
    
    # Build the model.
    text_model = markovify.NewlineText(text)
    
    # Print five randomly-generated sentences
    for i in range(5):
        print(text_model.make_sentence())




#-----------------------WIKI HOW BOT-----------------------
def getWinner():
    import urllib.request    
    url = "https://www.wikihow.com/Special:Randomizer"
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('utf-8')
    page_soup = Soup(data, "html.parser") 
    images = page_soup.findAll("img", {"class" : "whcdn content-fill"})
    title = page_soup.findAll("h1", {"id" : "section_0"})
    summary = page_soup.findAll("p")
    return [ title[0].text ,summary[5].text, "https://www.wikihow.com" + random.choice(images)["data-srclarge"] ] 

#-----------------------flag getter -----------------------------
def flagGetter(name):
    name = name.title()
    
    countries = {'Andorra': 'AD', 'United Arab Emirates': 'AE', 'Afghanistan': 'AF', 'Antigua and Barbuda': 'AG', 'Anguilla': 'AI', 'Albania': 'AL', 'Armenia': 'AM', 'Netherlands Antilles': 'AN', 'Angola': 'AO', 'Antarctica': 'AQ', 'Argentina': 'AR', 'American Samoa': 'AS', 'Austria': 'AT', 'Australia': 'AU', 'Aruba': 'AW', 'Ã\x85land Islands': 'AX', 'Azerbaijan': 'AZ', 'Bosnia and Herzegovina': 'BA', 'Barbados': 'BB', 'Bangladesh': 'BD', 'Belgium': 'BE', 'Burkina Faso': 'BF', 'Bulgaria': 'BG', 'Bahrain': 'BH', 'Burundi': 'BI', 'Benin': 'BJ', 'Saint BarthÃ©lemy': 'BL', 'Bermuda': 'BM', 'Brunei Darussalam': 'BN', 'Bolivia': 'BO', 'Bonaire, Sint Eustatius and Saba': 'BQ', 'Brazil': 'BR', 'Bahamas': 'BS', 'Bhutan': 'BT', 'Bouvet Island': 'BV', 'Botswana': 'BW', 'Belarus': 'BY', 'Belize': 'BZ', 'Canada': 'CA', 'Cocos (Keeling) Islands': 'CC', 'Congo, The Democratic Republic Of The': 'CD', 'Central African Republic': 'CF', 'Congo': 'CG', 'Switzerland': 'CH', "CÃ´te D'Ivoire": 'CI', 'Cook Islands': 'CK', 'Chile': 'CL', 'Cameroon': 'CM', 'China': 'CN', 'Colombia': 'CO', 'Costa Rica': 'CR', 'Cuba': 'CU', 'Cape Verde': 'CV', 'CuraÃ§ao': 'CW', 'Christmas Island': 'CX', 'Cyprus': 'CY', 'Czech Republic': 'CZ', 'Germany': 'DE', 'Djibouti': 'DJ', 'Denmark': 'DK', 'Dominica': 'DM', 'Dominican Republic': 'DO', 'Algeria': 'DZ', 'Ecuador': 'EC', 'Estonia': 'EE', 'Egypt': 'EG', 'Western Sahara': 'EH', 'Eritrea': 'ER', 'Spain': 'ES', 'Ethiopia': 'ET', '': 'XK', 'Finland': 'FI', 'Fiji': 'FJ', 'Falkland Islands (Malvinas)': 'FK', 'Micronesia, Federated States Of': 'FM', 'Faroe Islands': 'FO', 'France': 'FR', 'Gabon': 'GA', 'United Kingdom': 'GB', 'Grenada': 'GD', 'Georgia': 'GE', 'French Guiana': 'GF', 'Guernsey': 'GG', 'Ghana': 'GH', 'Gibraltar': 'GI', 'Greenland': 'GL', 'Gambia': 'GM', 'Guinea': 'GN', 'Guadeloupe': 'GP', 'Equatorial Guinea': 'GQ', 'Greece': 'GR', 'South Georgia and the South Sandwich Islands': 'GS', 'Guatemala': 'GT', 'Guam': 'GU', 'Guinea-Bissau': 'GW', 'Guyana': 'GY', 'Hong Kong': 'HK', 'Heard and McDonald Islands': 'HM', 'Honduras': 'HN', 'Croatia': 'HR', 'Haiti': 'HT', 'Hungary': 'HU', 'Indonesia': 'ID', 'Ireland': 'IE', 'Israel': 'IL', 'Isle of Man': 'IM', 'India': 'IN', 'British Indian Ocean Territory': 'IO', 'Iraq': 'IQ', 'Iran, Islamic Republic Of': 'IR', 'Iceland': 'IS', 'Italy': 'IT', 'Jersey': 'JE', 'Jamaica': 'JM', 'Jordan': 'JO', 'Japan': 'JP', 'Kenya': 'KE', 'Kyrgyzstan': 'KG', 'Cambodia': 'KH', 'Kiribati': 'KI', 'Comoros': 'KM', 'Saint Kitts And Nevis': 'KN', "Korea, Democratic People's Republic Of": 'KP', 'Korea, Republic of': 'KR', 'Kuwait': 'KW', 'Cayman Islands': 'KY', 'Kazakhstan': 'KZ', "Lao People's Democratic Republic": 'LA', 'Lebanon': 'LB', 'Saint Lucia': 'LC', 'Liechtenstein': 'LI', 'Sri Lanka': 'LK', 'Liberia': 'LR', 'Lesotho': 'LS', 'Lithuania': 'LT', 'Luxembourg': 'LU', 'Latvia': 'LV', 'Libya': 'LY', 'Morocco': 'MA', 'Monaco': 'MC', 'Moldova, Republic of': 'MD', 'Montenegro': 'ME', 'Saint Martin': 'MF', 'Madagascar': 'MG', 'Marshall Islands': 'MH', 'Macedonia, the Former Yugoslav Republic Of': 'MK', 'Mali': 'ML', 'Myanmar': 'MM', 'Mongolia': 'MN', 'Macao': 'MO', 'Northern Mariana Islands': 'MP', 'Martinique': 'MQ', 'Mauritania': 'MR', 'Montserrat': 'MS', 'Malta': 'MT', 'Mauritius': 'MU', 'Maldives': 'MV', 'Malawi': 'MW', 'Mexico': 'MX', 'Malaysia': 'MY', 'Mozambique': 'MZ', 'Namibia': 'NA', 'New Caledonia': 'NC', 'Niger': 'NE', 'Norfolk Island': 'NF', 'Nigeria': 'NG', 'Nicaragua': 'NI', 'Netherlands': 'NL', 'Norway': 'NO', 'Nepal': 'NP', 'Nauru': 'NR', 'Niue': 'NU', 'New Zealand': 'NZ', 'Oman': 'OM', 'Panama': 'PA', 'Peru': 'PE', 'French Polynesia': 'PF', 'Papua New Guinea': 'PG', 'Philippines': 'PH', 'Pakistan': 'PK', 'Poland': 'PL', 'Saint Pierre And Miquelon': 'PM', 'Pitcairn': 'PN', 'Puerto Rico': 'PR', 'Palestine, State of': 'PS', 'Portugal': 'PT', 'Palau': 'PW', 'Paraguay': 'PY', 'Qatar': 'QA', 'RÃ©union': 'RE', 'Romania': 'RO', 'Serbia': 'RS', 'Russian Federation': 'RU', 'Rwanda': 'RW', 'Saudi Arabia': 'SA', 'Solomon Islands': 'SB', 'Seychelles': 'SC', 'Sudan': 'SD', 'Sweden': 'SE', 'Singapore': 'SG', 'Saint Helena': 'SH', 'Slovenia': 'SI', 'Svalbard And Jan Mayen': 'SJ', 'Slovakia': 'SK', 'Sierra Leone': 'SL', 'San Marino': 'SM', 'Senegal': 'SN', 'Somalia': 'SO', 'Suriname': 'SR', 'South Sudan': 'SS', 'Sao Tome and Principe': 'ST', 'El Salvador': 'SV', 'Sint Maarten': 'SX', 'Syrian Arab Republic': 'SY', 'Swaziland': 'SZ', 'Turks and Caicos Islands': 'TC', 'Chad': 'TD', 'French Southern Territories': 'TF', 'Togo': 'TG', 'Thailand': 'TH', 'Tajikistan': 'TJ', 'Tokelau': 'TK', 'Timor-Leste': 'TL', 'Turkmenistan': 'TM', 'Tunisia': 'TN', 'Tonga': 'TO', 'Turkey': 'TR', 'Trinidad and Tobago': 'TT', 'Tuvalu': 'TV', 'Taiwan, Republic Of China': 'TW', 'Tanzania, United Republic of': 'TZ', 'Ukraine': 'UA', 'Uganda': 'UG', 'United States': 'US', 'Uruguay': 'UY', 'Uzbekistan': 'UZ', 'Holy See (Vatican City State)': 'VA', 'Saint Vincent And The Grenadines': 'VC', 'Venezuela, Bolivarian Republic of': 'VE', 'Virgin Islands, British': 'VG', 'Virgin Islands, U.S.': 'VI', 'Vietnam': 'VN', 'Vanuatu': 'VU', 'Wallis and Futuna': 'WF', 'Samoa': 'WS', 'Yemen': 'YE', 'Mayotte': 'YT', 'South Africa': 'ZA', 'Zambia': 'ZM', 'Zimbabwe': 'ZW'}
    
    for i in list(countries.keys()):
        if name in i:
            return "https://www.countryflags.io/{}/shiny/64.png".format(countries[i])
    return "flag not found"
    


#-----------------COUNTRY INFORMATION GETTER-------------------
def cCountry(name = "all"):
    
    if name.lower() == "us" or name.lower() == "united states":
        return cState()
    
    import urllib.request    
    url = "https://corona.lmao.ninja/v2/countries"
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    a = json.loads(infile)
    
    
    if name == "all":
        return a
    else:
        for i in a:
            if i["country"] == name.title():
                return i
    
    
def cGet():
    import urllib.request    
    url = "https://corona.lmao.ninja/v2/all"
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    a = json.loads(infile)
    return a    



#___________State Information Getter_______________________
def cState(state = "all"):
    import urllib.request    
    url = "https://corona.lmao.ninja/v2/states"
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    a = json.loads(infile)
    
    if state == "all":
        return a
    else:
        for i in a:
            if i["state"] == state.title():
                return i
        

#____________POKE GETTER__________________________________
def pokeGetter(name):
    import urllib.request    
    url = "https://www.pokemon.com/us/pokedex/{}".format(name)
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('utf-8')
    page_soup = Soup(data, "html.parser") 
    images = page_soup.findAll("img", {"width" : "728"})
    title = page_soup.findAll("p")
    title = title[0].text
    title = title.replace("                  ","")
    title = title.replace("\n"," ")
    title = title.replace(name.capitalize(),"It")
    title = title.replace("PokÃ©mon","creature")
    picture = page_soup.findAll("img", {"class" : "active"})
    return [title,picture[0]["src"]]




#___________uiowa announcements_______________________                                               NOT WORKING
def uiup():
    import urllib.request    
    url = "https://coronavirus.uiowa.edu/news"
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('utf-8')
    page_soup = Soup(data, "html.parser") 
    
    #images = page_soup.findAll("img", {"width" : "728"})
    news = page_soup.findAll("a")
    news = news[11:18]
    
    toReturn = []
    
    for i in news:
        toReturn.append( [ i.text.replace("\n","") , "https://coronavirus.uiowa.edu/" + i["href"]] )
    return toReturn





#___________https://sv443.net/jokeapi/category/any__________
#___________JOKE API________________________________________
def jokeApiCategory(category = "any"):
    import urllib.request    
    url = "https://sv443.net/jokeapi/category/{}".format(category)
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    a = json.loads(infile)    
    if a["type"] == "twopart":
        return [ a["category"],a["setup"],a["delivery"]]
    else:
        return [ a["category"],a["joke"]]
    
#_____________http://itsthisforthat.com/api.php?text______
#_____________START UP API________________________________
def startUp():
    import urllib.request    
    url = "http://itsthisforthat.com/api.php?text"
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('utf-8')
    page_soup = Soup(data, "html.parser") 
    return page_soup.text

#________https://corporatebs-generator.sameerkumar.website/_
#________CORPORATE JARGON___________________________________
def buzzWords():
    import urllib.request    
    url = "https://corporatebs-generator.sameerkumar.website"
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    a = json.loads(infile)
    return a["phrase"]
#_________https://cat-fact.herokuapp.com/facts_____________
#_________CAT FACTS________________________________________
def catFacts():
    import urllib.request    
    url = "https://cat-fact.herokuapp.com/facts"
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    a = json.loads(infile)
    return random.choice( a["all"])["text"]   

#_____https://api.adviceslip.com/advice___________________
#_____ADVICE API__________________________________________
def adviceApi():
    import urllib.request    
    url = "https://api.adviceslip.com/advice"
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    a = json.loads(infile)
    return a["slip"]["advice"]

#______________MYTHIC SPOILER____________________________
#_____API KEY ZGFudGVlbnRyb3V2aWNoQGdtYWlsLmNvbQ==_______


#___________JESUS API_______________________________
#___________________________________________________
def Jesus():
    import urllib.request    
    url = "https://jesusapi.000webhostapp.com/api/"
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    a = json.loads(infile)
    return [a["number"],a["link"]]



#______________TACO API____________________________
#__http://taco-randomizer.herokuapp.com/random/?full-taco=true_

def Taco():
    import urllib.request    
    url = "http://taco-randomizer.herokuapp.com/random/?full-taco=true"
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    a = json.loads(infile)
    return a


#wiki how bot___________________________________
#_______________________________________________

def getImages():
    import urllib.request    
    url = "https://www.wikihow.com/Special:Randomizer"
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('utf-8')
    page_soup = Soup(data, "html.parser") 
    images = page_soup.findAll("img", {"width" : "728"})
    
    title = page_soup.findAll("h1")[0].text
    
    fucked = True
    
    while fucked:
        try:
            image = random.choice(images)["src"]
            fucked = False
        except:
            try:
                image = random.choice(images)["data-src"]
                fucked = False
            except: 
                pass
                
    
    title = (title.encode('ascii', 'ignore')).decode("utf-8")
    
    return [title,image]


#___________MIXED DRINK API_______________________
#_________________________________________________

def ingredientSearch(ingredient):
    ingredient = ingredient.replace(" ","_")
    import urllib.request    
    url = "https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={}".format(ingredient)
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    a = json.loads(infile)
    
    throw = random.choice(a["drinks"])
    
    newDrink = {}
    
    newDrink["image"] = throw["strDrinkThumb"]
    newDrink["name"] = throw["strDrink"]
    newDrink["ID"] = throw["idDrink"]
    

    
    
    url = "https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={}".format(newDrink["ID"])
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    a = json.loads(infile)   
    
    ingredients = ""
    
    for i in range(15):
        if i == 0:
            pass
        else:
            if a["drinks"][0]["strIngredient{}".format(str(i))] != None:
                ingredients += a["drinks"][0]["strIngredient{}".format(str(i))] + "\n"
                
    newDrink["ingredients"] = ingredients
    newDrink["recipe"] = a["drinks"][0]["strInstructions"]
    
    
    
    return newDrink
#______________numbers API_________________________
#__________________________________________________
def mathTrivia(nuber):
    import urllib.request    
    url = "http://numbersapi.com/{}/trivia".format(nuber)
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('utf-8') # Read the content as string decoded with utf-8
    page_soup = Soup(data, "html.parser") #html parsing
    return page_soup


def mathFact(nuber):
    import urllib.request    
    url = "http://numbersapi.com/{}/math".format(nuber)
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('utf-8') # Read the content as string decoded with utf-8
    page_soup = Soup(data, "html.parser") #html parsing
    return page_soup

def numberFact(nuber):
    import urllib.request    
    url = "http://numbersapi.com/{}".format(nuber)
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('utf-8') # Read the content as string decoded with utf-8
    page_soup = Soup(data, "html.parser") #html parsing
    return page_soup

def dateFact(nuber):
    import urllib.request    
    url = "http://numbersapi.com/{}/date".format(nuber)
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('utf-8') # Read the content as string decoded with utf-8
    page_soup = Soup(data, "html.parser") #html parsing
    return page_soup

def randomYear():
    import urllib.request    
    url = "http://numbersapi.com/random/year"
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('utf-8') # Read the content as string decoded with utf-8
    page_soup = Soup(data, "html.parser") #html parsing
    return page_soup

def randomDate():
    import urllib.request    
    url = "http://numbersapi.com/random/date"
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('utf-8') # Read the content as string decoded with utf-8
    page_soup = Soup(data, "html.parser") #html parsing
    return page_soup