from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Soup
import random
import json
import fuckyou
from fuckyou import *
import re

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
    data = infile.decode('ISO-8859-1')
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
#_____https://yesno.wtf/api/______________________________
#_____YES NO API__________________________________________
def yesNoApi():
    import urllib.request    
    url = "https://yesno.wtf/api/"
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    a = json.loads(infile)
    return [ a["answer"] , a["image"] ]    

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


#______________shinobi api key eebc1e9ad5204636a5d4e24dd79a2d6c ______________
#______________SHINOBI API THING______________________________________________

##______________________________movie rating getter from IMDB_________________
##____________________________________________________________________________
def movieRating(name):
    
    import xmltodict
    import urllib.request 
    name = name.replace(" ","%20")
    url = "https://api.hillbillysoftware.com/Rating/ByName/eebc1e9ad5204636a5d4e24dd79a2d6c/{}".format(name)
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    a = json.loads(infile)
    a=a[0]
    return [a["Name"],a["IMDB"],a["imdbID"]]

##______________________________movie rating getter from IMDB_________________
##____________________________________________________________________________
def artistInformation(name):
    try:
        import xmltodict
        import urllib.request 
        name = name.replace(" ","%20")
        url = "https://api.hillbillysoftware.com/Music/Artist/Extended/eebc1e9ad5204636a5d4e24dd79a2d6c/{}".format(name)
        page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
        infile=urllib.request.urlopen(page).read()
        a = json.loads(infile)
        
        albums = "{}'s Albums:{}".format(a["Name"],"\n")
        
        for i in a["Albums"]:
            albums += " {} - released {}{}".format(i["Name"],i["Releaseyear"],"\n")
        print(albums)
            
            
        
        
        
        
        return [a["Genre"],a["Name"],a["FormationYear"],a["Biography"][:250]+"...",a["WebSite"],a["Logo"]]
    except:
        return "oh no"
    
    
#____________BIBLE BOT___________________________________
#___________API KEY fb56b98ed9f3f5b3dae54820daeda829 ____
#________________________________________________________

def OwOBle(passage):

    
    
    passage = passage.replace(" ","")
    passage = passage.replace(":",".")
    
    #use fuckdick(message)
    import urllib.request    
    url = "http://api.biblia.com/v1/bible/content/LEB.txt.txt?passage={}&callback=myCallbackFunction&key=fd37d8f28e95d3be8cb4fbc37e15e18e".format(passage)
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()   
    data = infile.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1
    page_soup = Soup(data, "html.parser") #html parsing
    return fuck(page_soup.text)
    

import spacy


def melble():    

    
    #use fuckdick(message)
    import urllib.request    
    url = "http://labs.bible.org/api/?passage=random"
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()   
    data = infile.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1
    page_soup = Soup(data, "html.parser") #html parsing
    passage = page_soup.text
    
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(passage)
    
    toReturn = ""
    
    nouns = ["NOUN"]
    
    import random
    
    for token in doc:
        if token.pos_ in nouns and random.randint(0,1) == 1:
            toReturn += " {}".format("Mel")
        else:
            toReturn += " {}".format(token)
    return toReturn
    
    


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
    data = infile.decode('ISO-8859-1')
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



#___________MTG PRICE GETTER______________________
#_________________________________________________
def cardPrice(cunt):
    import urllib.request
    
    cardInfo = {}
    cardInfo["name"] = cunt
    
    cunt = cunt.replace(" ","-")
    cunt = cunt.replace("'","")
    
    url = "https://tappedout.net/mtg-card/{}/".format(cunt)
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1
    page_soup = Soup(data, "html.parser") #html parsing
    Whole = page_soup.findAll("div", {"class": "col-sm-6"})
    
    g = []
    
    for i in Whole:
        g.append( i.text )
    
    for i in range(len(g)):
        g[i] = g[i].split("\n\n\n")
        
    for i in range(len(g)):
        for fuck in range(len(g[i])):
            g[i][fuck] = g[i][fuck].replace("\n","")
            g[i][fuck] = re.sub(r'\s+', ' ', g[i][fuck])
    
    prices = []
    
    for i in g:
        for fuck in i:
            if len(fuck) > 0 and bool(re.search(r'\d', fuck)):
                prices.append(fuck)
    
    

    
    
    cardInfo["prices"] = prices
    
    
    
    
    
    
    return cardInfo


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
    data = infile.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1
    page_soup = Soup(data, "html.parser") #html parsing
    return page_soup


def mathFact(nuber):
    import urllib.request    
    url = "http://numbersapi.com/{}/math".format(nuber)
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1
    page_soup = Soup(data, "html.parser") #html parsing
    return page_soup

def numberFact(nuber):
    import urllib.request    
    url = "http://numbersapi.com/{}".format(nuber)
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1
    page_soup = Soup(data, "html.parser") #html parsing
    return page_soup

def dateFact(nuber):
    import urllib.request    
    url = "http://numbersapi.com/{}/date".format(nuber)
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1
    page_soup = Soup(data, "html.parser") #html parsing
    return page_soup

def randomYear():
    import urllib.request    
    url = "http://numbersapi.com/random/year"
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1
    page_soup = Soup(data, "html.parser") #html parsing
    return page_soup

def randomDate():
    import urllib.request    
    url = "http://numbersapi.com/random/date"
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1
    page_soup = Soup(data, "html.parser") #html parsing
    return page_soup
    
    
#RANDOM MOVIE GETTER
    
def weedDictMaker(dicle):
    
    from collections import defaultdict
    
    import pickle
    
    #A dict with all races
    races = defaultdict(list)
    
    #A dict with all flavors
    flavors = defaultdict(list)
    
    #A Dict with all effects
    effects = defaultdict(list)
    
    #A Dict with all the fucking strains
    with open('AllStrains.pickle', 'wb') as handle:
        pickle.dump(dicle, handle, protocol=pickle.HIGHEST_PROTOCOL)     
    
    
    for i in list(dicle.keys()):
        
        name = i
        
        i = dicle[i]
        i["name"] = name
        
        #ASSIGN FOR RACES
        races[i["race"]].append(i)
        
        
 
        for taste in i["flavors"]:
            flavors[taste].append(i)
            
        for effect in i["effects"]["positive"]:
            effects[effect].append(i)
                    
        for effect in i["effects"]["negative"]:
            effects[effect].append(i)

                
    
    
    
    with open('WEED_EFFECTS.pickle', 'wb') as handle:
        pickle.dump(effects, handle, protocol=pickle.HIGHEST_PROTOCOL)   
    with open('WEED_FLAVORS.pickle', 'wb') as handle:
        pickle.dump(flavors, handle, protocol=pickle.HIGHEST_PROTOCOL)      
    with open('WEED_RACES.pickle', 'wb') as handle:
        pickle.dump(races, handle, protocol=pickle.HIGHEST_PROTOCOL)      




        {'id': 1, 'race': 'hybrid', 'flavors': ['Earthy', 'Chemical', 'Pine'], 'effects': {'positive': ['Relaxed', 'Hungry', 'Happy', 'Sleepy'], 'negative': ['Dizzy'], 'medical': ['Depression', 'Insomnia', 'Pain', 'Stress', 'Lack of Appetite']}, 'name': 'Afpak'}




 
 
def massCombine():
    import pickle
    import operator
    my_dict_final = {}  # Create an empty dictionary
    my_dict_final["results"] = []
    first = 0
    second = 250
    result = []
    
    g = 355
    
    for i in range(g):
        f = pickle.load( open( "{}-{}.pickle".format(first,second), "rb" ) )
        result = operator.add(result , f["results"])
        first += 250
        second += 250
    
    my_dict_final["results"] = result

   
    
    pickle.dump( my_dict_final, open( "save.pickle", "wb" ) )
    

def test1():
    from collections import defaultdict
    import pickle
    import operator
    toReturn = defaultdict(list)
    first = 0
    second = 250
    result = []
    
    g = 355
    
    for i in range(1):
        #go through each movie
        currMovie = pickle.load( open( "{}-{}.pickle".format(first,second), "rb" ) )
        for movie in currMovie["results"]:
            #get the IMDB results for the movie
            results = imdBRO( movie["imdb"] )
            
            for genre in results[1]:
                toReturn[genre].append(movie)
            
            
        
        first += 250
        second += 250

   
    
    pickle.dump( my_dict_final, open( "testing1.pickle", "wb" ) )    

    



    
    

def imdBRO(ID):
    import urllib.request    
    url = "https://www.imdb.com/title/{}/".format(ID)
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('ISO-8859-1')
    page_soup = Soup(data, "html.parser") 
    
    
    rating = page_soup.findAll("span", {"itemprop" : "ratingValue"})
    rating = rating[0].text
    
    genre = page_soup.findAll("div", {"class" : "see-more inline canwrap"})
    genre = genre[-1].text.replace("\xa0|","").split("\n")
    fuck = []
    for i in genre:
        if len(i) > 1 and i != "Genres:":
            fuck.append(i.strip())
    genre = fuck
    
    return [rating, genre]
    
    
    
    #movies["results"][0]
    #{'id': 172052, 'title': 'Midsommar', 'release_year': 2019, 'themoviedb': 530385, 'original_title': 'Midsommar', 'alternate_titles': ["Midsommar Director's Cut", 'Midsommar (Commentary Version)'], 'imdb': 'tt8772262', 'pre_order': False, 'in_theaters': False, 'release_date': '2019-07-03', 'rating': 'R', 'rottentomatoes': 0, 'freebase': '', 'wikipedia_id': 0, 'metacritic': None, 'common_sense_media': None, 'poster_120x171': 'http://static-api.guidebox.com/100117/thumbnails_movies_small/172052-7939682943-3051673109-273224656-small-120x171.jpg', 'poster_240x342': 'http://static-api.guidebox.com/100117/thumbnails_movies_medium/172052-5821764506-2734788549-7699393155-medium-240x342.jpg', 'poster_400x570': 'http://static-api.guidebox.com/100117/thumbnails_movies/172052-3780710520-8723092307-4108234583-large-400x570.jpg'}
    #movies["results"][1]
    #{'id': 175823, 'title': 'Doom: Annihilation', 'release_year': 2019, 'themoviedb': 520901, 'original_title': 'Doom: Annihilation', 'alternate_titles': ['Untitled Doom Reboot', 'Doom Reboot'], 'imdb': 'tt8328716', 'pre_order': False, 'in_theaters': False, 'release_date': '2019-10-01', 'rating': 'R', 'rottentomatoes': 0, 'freebase': '', 'wikipedia_id': 0, 'metacritic': None, 'common_sense_media': None, 'poster_120x171': 'http://static-api.guidebox.com/100117/thumbnails_movies_small/175823-8110106494-4530839059-5817995546-small-120x171.jpg', 'poster_240x342': 'http://static-api.guidebox.com/100117/thumbnails_movies_medium/175823-9741843780-8585053347-5537037998-medium-240x342.jpg', 'poster_400x570': 'http://static-api.guidebox.com/100117/thumbnails_movies/-175823-4711535601-9528716667-7747535966-large-400x570.jpg'}
    #movies["results"][3]
    #{'id': 172027, 'title': 'Spider-Man: Far from Home', 'release_year': 2019, 'themoviedb': 429617, 'original_title': 'Spider-Man: Far from Home', 'alternate_titles': ['Spider-Man: Homecoming 2', 'Spider-Man 4', 'Spider-Man: Far From Home (2019)', 'Spider-Man: Far From Home [Bonus]', 'Spider-Man: Far From Home [4K UHD]', 'Spider-Man: Far From Home – Extended Cut'], 'imdb': 'tt6320628', 'pre_order': False, 'in_theaters': True, 'release_date': '2019-06-28', 'rating': 'PG-13', 'rottentomatoes': 771458355, 'freebase': '', 'wikipedia_id': 52179698, 'metacritic': 'http://www.metacritic.com/https://www.metacritic.com/movie/spider-man-far-from-home', 'common_sense_media': 'https://www.commonsensemedia.org/movie-reviews/spider-man-far-from-home', 'poster_120x171': 'http://static-api.guidebox.com/100117/thumbnails_movies_small/172027-1482369877-9921749476-2933556107-small-120x171-alt-.jpg', 'poster_240x342': 'http://static-api.guidebox.com/100117/thumbnails_movies_medium/172027-106347702-6942055267-5612275479-medium-240x342-alt-.jpg', 'poster_400x570': 'http://static-api.guidebox.com/100117/thumbnails_movies/-alt--172027-9782975753-6315151369-1781409858-large-400x570-alt-.jpg'}
    #movies["results"][4]
    #{'id': 173757, 'title': 'Crawl', 'release_year': 2019, 'themoviedb': 511987, 'original_title': 'Crawl', 'alternate_titles': ['Crawl (2019)'], 'imdb': 'tt8364368', 'pre_order': False, 'in_theaters': False, 'release_date': '2019-07-11', 'rating': 'R', 'rottentomatoes': 0, 'freebase': '', 'wikipedia_id': 0, 'metacritic': None, 'common_sense_media': 'https://www.commonsensemedia.org/movie-reviews/crawl', 'poster_120x171': 'http://static-api.guidebox.com/100117/thumbnails_movies_small/173757-740748826-3513059155-7740932316-small-120x171.jpg', 'poster_240x342': 'http://static-api.guidebox.com/100117/thumbnails_movies_medium/173757-7707622372-2684930791-6439709808-medium-240x342.jpg', 'poster_400x570': 'http://static-api.guidebox.com/100117/thumbnails_movies/173757-9194359374-6067223186-5663427771-large-400x570.jpg'}
    #movies["results"][5]
    #{'id': 170578, 'title': 'Aladdin', 'release_year': 2019, 'themoviedb': 420817, 'original_title': 'Aladdin', 'alternate_titles': ['Aladdin (2019)', 'Aladdin (Plus Bonus Content)'], 'imdb': 'tt6139732', 'pre_order': False, 'in_theaters': True, 'release_date': '2019-05-22', 'rating': 'NR', 'rottentomatoes': 0, 'freebase': '', 'wikipedia_id': 54681061, 'metacritic': 'http://www.metacritic.com/https://www.metacritic.com/movie/aladdin-2019', 'common_sense_media': 'https://www.commonsensemedia.org/movie-reviews/aladdin-0', 'poster_120x171': 'http://static-api.guidebox.com/100117/thumbnails_movies_small/170578-9903501486-9870248404-4242343605-small-120x171.jpg', 'poster_240x342': 'http://static-api.guidebox.com/100117/thumbnails_movies_medium/170578-4724518904-9702768521-8637603121-medium-240x342.jpg', 'poster_400x570': 'http://static-api.guidebox.com/100117/thumbnails_movies/-170578-3451640066-3518252727-7189153116-large-400x570.jpg'}
    #movies["results"][6]
    #{'id': 175713, 'title': 'In the Shadow of the Moon', 'release_year': 2019, 'themoviedb': 530382, 'original_title': 'In the Shadow of the Moon', 'alternate_titles': [], 'imdb': 'tt8110640', 'pre_order': False, 'in_theaters': False, 'release_date': '2019-09-21', 'rating': 'NR', 'rottentomatoes': 771496160, 'freebase': '', 'wikipedia_id': 57692145, 'metacritic': 'http://www.metacritic.com/https://www.metacritic.com/movie/in-the-shadow-of-the-moon-2019', 'common_sense_media': 'https://www.commonsensemedia.org/movie-reviews/in-the-shadow-of-the-moon', 'poster_120x171': 'http://static-api.guidebox.com/100117/thumbnails_movies_small/175713-9926521703-868844940-5603673188-small-120x171.jpg', 'poster_240x342': 'http://static-api.guidebox.com/100117/thumbnails_movies_medium/175713-7229031399-3389798612-9748292979-medium-240x342.jpg', 'poster_400x570': 'http://static-api.guidebox.com/100117/thumbnails_movies/175713-2059499212-3152841022-3975029877-large-400x570.jpg'}


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


def fuckYouToo(number):
    import urllib.request    
    url = "https://www.codechef.com/problems/easy/"
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('ISO-8859-1')
    page_soup = Soup(data, "html.parser") 
    
    #getting names
    names = page_soup.findAll("div", {"class" : "problemname"})
    for i in range(len(names)):
        names[i] = names[i].text.replace("\n","")
   
    #getting problem codes
    codes = page_soup.findAll("a", {"title" : "Submit a solution to this problem."})
    for i in range(len(codes)):
        codes[i] = codes[i].text.replace("\n","")    
    #getting accuracy of submission
    percentAccuracy = page_soup.findAll("a", {"title" : "See all submitted solutions to this problem."})
    for i in range(len(percentAccuracy)):
        percentAccuracy[i] = percentAccuracy[i].text.replace("\n","")    
    
    
    fuck = {}
    for i in range(len(codes)):
        
        if(names[i] !="Chef and Soccer"):
        
            fuck[names[i]] = [codes[i] , percentAccuracy[i]]
    
    print( fuck )
    