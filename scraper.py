import pandas as pd
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests
def scrapdata(link,fullinfo):
    i = 1
    #fullinfo = pd.DataFrame({'branza': [], 'nazwa': [], 'strona': [], 'email': [], 'telefon': []})
    while True:
        if (i == 1):
            URL = "https://panoramafirm.pl/"+link
        else:
            URL = "https://panoramafirm.pl/"+link+"/firmy,"+str(i)+".html"
        r = requests.get(URL)
        print(i)
        print(URL)
        soup = BeautifulSoup(r.content, 'html.parser')
        matching = soup.find("ul", class_='list-unstyled')
        new1 = matching.find_all(class_='company-item')
        # control if we reached the end
        if new1==[] :
            print("reached the end")
            break
        i+=1

        for elem in new1:

            title = elem.find('a', {'class': 'company-name'})
            website1 = elem.find('a', {'class': 'icon-website'})
            website = website1.get('href')
            email1 = elem.find('a', {'class': 'addax-cs_hl_email_submit_click'})
            email = email1.get('data-company-email')
            telefon1 = elem.find('a', {'class': 'addax-cs_hl_phonenumber_click'})
            telefon = telefon1.get('title')
            if (website != None or email != None or telefon != None ):
                    fullinfo = fullinfo.append(
                            {'branza': link, 'nazwa': title.text, 'strona': website, 'email': email, 'telefon': telefon}, ignore_index=True)
    return fullinfo

