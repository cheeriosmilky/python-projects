from typing import Text
from bs4 import BeautifulSoup
import requests

city = "Weather in Boardman Ohio"
url = f"https://www.google.com/search?q={city}"
html = requests.get(url).content
httppull = BeautifulSoup(html, "html.parser")
temp = httppull.find("div", class_ = "BNeawe iBp4i AP7Wnd").text.strip('°F')

if int(temp) >= 90:
    print(f'Temp is {temp}°F, too hot.')
elif int(temp) > 65 < 90:
    print(f'Temp is {temp}°F, just right')
else:
    print(f'Temp is {temp}°F, too cold')
