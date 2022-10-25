from typing import Text
from bs4 import BeautifulSoup
import requests

city = "Weather in Boardman Ohio"
url = f"https://www.google.com/search?q={city}"
html = requests.get(url).content
httppull = BeautifulSoup(html, "html.parser")
temp = httppull.find("div", class_ = "BNeawe").text
skystatus = httppull.find("div", class_ = 'BNeawe s3v9rd AP7Wnd').text
feelstatus = httppull.find("div", class_ = 'BNeawe tAd8D AP7Wnd').text

print(f"Tempature: {temp}")
print(f"Description: {skystatus}\n{feelstatus}")