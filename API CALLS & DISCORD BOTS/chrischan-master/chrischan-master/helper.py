from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Soup
import random



#__________________________________________________
#____________Become a Christorian__________________
def rabbitHole():
    link = "https://sonichu.com/cwcki/Saga"
    image = "https://files.catbox.moe/7ieudt.jpg"
    return [link,image]





#___________________________________________
#____________QUOTE OF THE NOW_______________ WORKING

def quoteOfTheNow():
    
    
    import urllib.request    
    url = "https://sonichu.com/cwcki/Main_Page"
    
    update = ""
    
    # Open the URL as Browser, not as python urllib
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1
    page_soup = Soup(data, "html.parser") #html parsing
    
    Whole = page_soup.findAll("td", {"style": "color:#000;"})
    update = Whole[4].text
    update = update.replace("\n","")
    
    update = (update.encode('ascii', 'ignore')).decode("utf-8")
    
#    images.append( hentai.a.img["data-src"])


        
    
#    images.append( hentai.a.img["data-src"])

    return update




#___________________________________________
#____________Chris chan begging stats_______________ WORKING

def chrisChanBegging():
    
    import urllib.request    
    url = "https://sonichu.com/cwcki/Main_Page"
    
    update = ""
    
    # Open the URL as Browser, not as python urllib
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1
    page_soup = Soup(data, "html.parser") #html parsing
    
    Whole = page_soup.findAll("td", {"style": "color:#000;"})
    update = Whole[0].text
    
    update = update.replace("\n","")
    update = (update.encode('ascii', 'ignore')).decode("utf-8")
    update = update.split(".")
    update = update[:-1]
    
#    images.append( hentai.a.img["data-src"])


        
    
#    images.append( hentai.a.img["data-src"])

    return update







#___________________________________________________
#____________this day is in christory_______________ WORKING

def thisDayInChristory():
    
    
    import urllib.request    
    url = "https://sonichu.com/cwcki/Main_Page"
    
    update = ""
    
    # Open the URL as Browser, not as python urllib
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1
    page_soup = Soup(data, "html.parser") #html parsing
    
    Whole = page_soup.findAll("td", {"style": "color:#000;"})
    update = Whole[2].text
    update = update.replace("\n","")
    update = update.replace("(more...)","")
    update = (update.encode('ascii', 'ignore')).decode("utf-8")
#    images.append( hentai.a.img["data-src"])


        
    
#    images.append( hentai.a.img["data-src"])

    return update




#___________________________________________
#____________Did you know?__________________

def didYouKnow():
    
    import urllib.request    
    url = "https://sonichu.com/cwcki/Main_Page"
    
    update = ""
    
    # Open the URL as Browser, not as python urllib
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1
    page_soup = Soup(data, "html.parser") #html parsing
    
    Whole = page_soup.findAll("td", {"style": "color:#000;"})
    update = Whole[3].text
    update = update.replace("\n","")
    update = (update.encode('ascii', 'ignore')).decode("utf-8")
    update = update.split("...")
    update = update[1:]

    
#    images.append( hentai.a.img["data-src"])


        
    
#    images.append( hentai.a.img["data-src"])

    return update



#___________________________________________
#____________Article of the now_____________

def articleOfTheNow():
    
    
    import urllib.request    
    url = "https://sonichu.com/cwcki/Main_Page"
    
    update = ""
    
    # Open the URL as Browser, not as python urllib
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1
    page_soup = Soup(data, "html.parser") #html parsing
    
    Whole = page_soup.findAll("td", {"style": "color:#000;"})
    update = Whole[1].text
    update = update.replace("\n","")
    update = (update.encode('ascii', 'ignore')).decode("utf-8")
    
#    images.append( hentai.a.img["data-src"])

    return [update,url]




#___________________________________________________
#____________Quick Article Rundown__________________

def articleSummary(name):
    link = ""
    
    import urllib.request    
    name = name.replace(" ", "_")
    url = "https://sonichu.com/cwcki/" + name
    try:
        update = ""
        
        # Open the URL as Browser, not as python urllib
        page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
        infile=urllib.request.urlopen(page).read()
        data = infile.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1
        page_soup = Soup(data, "html.parser") #html parsing
        
        Whole = page_soup.findAll("p")
        for i in Whole:
            if i != None:
                if len(i) > 5:
                    update = update + i.text
                
        update = str(update)
        update = update[:600]
        g = update.find("restoring these links")
        if g == None:
            g = -22
        update = update[g+22:]
    #    images.append( hentai.a.img["data-src"])
    
        return[update,url]
    except Exception as e:
        print (e)
        return ["Hey we ran into an error with the article name provided, the CWCKI isn't forgiving and is poorly coded. if you are looking for Shrek retold, try Shrek Retold","google.com"]

