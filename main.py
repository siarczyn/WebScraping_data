import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

URL = "https://panoramafirm.pl/salony_i_gabinety_kosmetyczne?sort=1"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html.parser')
matching = soup.find("ul", class_='list-unstyled')
new1 = matching.find_all(class_='company-item')
df = pd.DataFrame({'nazwa': [], 'strona': [], 'email': [], 'telefon': []})

for elem in new1:
    title = elem.find('a', {'class': 'company-name'})
    website1 = elem.find('a', {'class': 'icon-website'})
    website = website1.get('href')
    email1 = elem.find('a', {'class': 'addax-cs_hl_email_submit_click'})
    email = email1.get('data-company-email')
    telefon1 = elem.find('a', {'class': 'addax-cs_hl_phonenumber_click'})
    telefon = telefon1.get('title')
    df = df.append({'nazwa': title.text, 'strona': website, 'email': email, 'telefon': telefon}, ignore_index=True)
df.to_excel("output.xlsx")
print(df)