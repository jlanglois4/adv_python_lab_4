import requests
from bs4 import BeautifulSoup

URL = 'https://tolkienconference.com/expo-speakers/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
items = soup.find_all('div', class_="name")
name_list = []
for name in items:
    name_list.append(name.string)
# Print Out Data
for name in name_list:
    print(name)
