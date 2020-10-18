from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Soup
import random
import json
import pickle
import urllib.request

def getFox(site = "https://www.foxnews.com", section = "politics" ):
    #get the site and section
    url = "{}/{}".format(site,section)
    
    #Get the HTML
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('utf-8')
    page_soup = Soup(data, "html.parser") 
    
    #search for the titles
    titles = page_soup.findAll("h2", {"class" : "title"})
    
    return titles

def getBabylonBee(site = "https://babylonbee.com", section = "" ):
    #get the site and section
    url = "{}/{}".format(site,section)

    
    #Get the HTML
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('utf-8')
    page_soup = Soup(data, "html.parser") 
    

    #search for the titles
    titles = page_soup.findAll("div" , { "class" : "col-sm-6"})
    latest = titles[1].findAll("a")
    toReturn = []
    for i in latest:
        x = i.text.strip()
        y = x.index("\n")
        toReturn.append( [ "https://babylonbee.com"+i["href"], x[:y]] )
    
    return toReturn

def getOnion(site = "https://www.theonion.com", section = "latest" ):
    #get the site and section
    url = "{}/{}".format(site,section)

    
    #Get the HTML
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('utf-8')
    page_soup = Soup(data, "html.parser") 
    
    titles = page_soup.findAll( "a" , { "class" : "sc-1out364-0 hMndXN js_link" } )
    titles = titles[14:]
    toReturn = []
    for i in range(0 , 7, 2):
        x = titles[i].text
        y = titles[i]["href"]
        toReturn.append( [y,x] )
    return toReturn


def getTheSpoof(site = "https://www.thespoof.com/", section = "spoof-news/us/" ):
    #get the site and section
    url = "{}/{}".format(site,section)

    
    #Get the HTML
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('utf-8')
    page_soup = Soup(data, "html.parser") 
    title = page_soup.findAll("div", {"class" : "short story"})
    toReturn = []
    for i in title:
        x = i.a.h2.text
        y = "https://www.thespoof.com" + i.a["href"]
        
        toReturn.append( [ y , x ] )
    
    return toReturn


def getSatire():
    toReturn = []
    toReturn.append( getOnion() )
    toReturn.append( getBabylonBee() )
    toReturn.append( getTheSpoof() )
    return toReturn
