import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

for i in range(1,1838):
    if (i==1):
        URL = "https://panoramafirm.pl/salony_i_gabinety_kosmetyczne"
    else:
        URL = "https://panoramafirm.pl/salony_i_gabinety_kosmetyczne/firmy,"+str(i)+".html"
    r = requests.get(URL)
    print(i)
    soup = BeautifulSoup(r.content, 'html.parser')
    matching = soup.find("ul", class_='list-unstyled')
    new1 = matching.find_all(class_='company-item')
    df = pd.DataFrame({'nazwa': [], 'strona': [], 'email': [], 'telefon': []})
    onlyPhones = pd.DataFrame({'nazwa': [], 'strona': [], 'email': [], 'telefon': []})

    for elem in new1:

        title = elem.find('a', {'class': 'company-name'})
        website1 = elem.find('a', {'class': 'icon-website'})
        website = website1.get('href')
        email1 = elem.find('a', {'class': 'addax-cs_hl_email_submit_click'})
        email = email1.get('data-company-email')
        telefon1 = elem.find('a', {'class': 'addax-cs_hl_phonenumber_click'})
        telefon = telefon1.get('title')
        if (website != "None"):
            if (email != "None" or telefon != "None"):
                df = df.append({'nazwa': title.text, 'strona': website, 'email': email, 'telefon': telefon}, ignore_index=True)
            if (email == "None" and telefon != "None"):
                onlyPhones = onlyPhones.append({'nazwa': title.text, 'strona': website, 'email': email, 'telefon': telefon},
                               ignore_index=True)
df.to_excel("output.xlsx")
onlyPhones.to_excel("Only_telephones.xlsx")
