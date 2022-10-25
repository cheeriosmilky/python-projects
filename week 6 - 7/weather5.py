from cgitb import html
from urllib.request import urlopen
from bs4 import BeautifulSoup
# import requests

url = "https://www.wunderground.com/forecast/us/oh/boardman/KYNG"

requestpage = urlopen(url)
phtml = requestpage.read()
requestpage.close()

httppull = BeautifulSoup(phtml, 'html.parser')
temp = httppull.find_all('div', class_ = "charts-header pan-viewport")

for daytemps in temp:
    day = daytemps.find_all('a', class_ = 'navigate-to ng-star-inserted')
    hitemp = daytemps.find('span', class_ = 'temp-hi')
    lotemp = daytemps.find('span', class_ = 'temp-lo')

print(temp)