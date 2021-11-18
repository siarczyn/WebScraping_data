from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
import requests
from scraper import scrapdata
import string

web = webdriver.Firefox()
web.implicitly_wait(10)
web.get('https://panoramafirm.pl/branze/lista.html')
sleep(5)
r = web.page_source
soup = BeautifulSoup(r, 'html.parser')
matching = soup.find("div", id='trade-groups-list')
print(matching)
all_branches = matching.find_all("h2")
list_of_branches = []
 #dziala licznik katalogu branz
#scrapdata(all_branches)
for i in range(0, len(all_branches)): #loop for going through all branches
    letters1 = soup.find("ul",class_="letters-index")
    letters = letters1.find_all("li")
    #print(letters)
    for y in range(0, len(letters)): #loop going through all letters in branch
        print(letters[y].text.strip())
        match = soup.find("div", id='letter-'+letters[y].text.strip()+'-card')
        ul = match.find("ul")
        website1 = ul.find('a')
        website = website1.get('href')
        print(website)
