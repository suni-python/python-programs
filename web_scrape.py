#Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup as bs

url="https://www.nytimes.com/"
data=requests.get(url)
soup=bs(data.text,'html.parser')
for l in soup.find_all('h2'):
    print(l.string)


