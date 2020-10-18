from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome(executable_path=r"C:\Users\white\Desktop\NEW BOTS\pokeman\chromedriver.exe")
browser.get("https://discordapp.com/login")

email = "nibbalumj@gmail.com"
password = "!Q2w3e4r5t"


def catchPokemon(msg):
    email_input = browser.find_element_by_xpath('//textarea')
    email_input.send_keys(msg)    
    email_input.send_keys(Keys.RETURN)