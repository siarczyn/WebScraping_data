from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
import requests
from scraper import scrapdata
import string
# web = webdriver.Firefox()
# web.implicitly_wait(10)
# web.get('https://panoramafirm.pl/branze/lista.html')
# sleep(3)
# cookies = web.find_element_by_xpath('//*[@id="cookie-disable"]')
# cookies.click()
# r = web.page_source
r = requests.get('https://panoramafirm.pl/branze/lista.html')
soup = BeautifulSoup(r.content, 'html.parser')
matching = soup.find("div", id='trade-groups-list')
all_branches = matching.find_all("h2")
OgBranchList = matching.find_all("a")

print(all_branches[1].text)
print(all_branches)
list_of_branches = []
fullinfo = pd.DataFrame({'OGBranch':[],'branch': [], 'nazwa': [], 'strona': [], 'email': [], 'telefon': []})

for i in range(0, len(all_branches)):
    OgBranchList = matching.find_all("a")
    OgBranchList = OgBranchList[i].get("href")
    print(OgBranchList)
    r = requests.get("https://panoramafirm.pl"+OgBranchList)
    soup = BeautifulSoup(r.content, 'html.parser')
    #for i in range(0, len(all_branches)): #loop for going through all branches
    letters1 = soup.find("ul",class_="letters-index")
    letters = letters1.find_all("li")
    #print(letters)
#    for y in range(0, 1):
    for y in range(0, len(letters)): #loop going through all letters in branch
        print(letters[y].text.strip())
        match = soup.find("div", id='letter-'+letters[y].text.strip()+'-card')
        ul = match.find("ul")
        website1 = ul.find('a')
        website = website1.get('href')
        print(website)
        fullinfo = scrapdata(website,all_branches[i],fullinfo)

fullinfo.to_excel("dawajfullinfo.xlsx")
