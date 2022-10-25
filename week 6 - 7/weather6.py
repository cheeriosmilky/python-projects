from logging.config import fileConfig
from bs4 import BeautifulSoup
import requests
url = 'https://weather.com/weather/today/l/b5898a548a77ef416b735bebad9f9a4458341248ee95bda165f9441aa82cb959'
html = requests.get(url).content
httppull = BeautifulSoup(html, 'html.parser')
print('Next 5 Days of Weather: ')
days = httppull.find_all('div', class_ = 'Column--temp--5hqI_')
fivedays = days[-5:]
for i in fivedays:
    alldays = httppull.find_all('div', class_ = 'TemperatureValue')
    print(i.string)