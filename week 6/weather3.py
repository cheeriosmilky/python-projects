from typing import Text
from bs4 import BeautifulSoup
import requests

city = "Boardman Ohio"
url = "https://www.google.com/search?q="+"weather"+city
html = requests.get(url).content
httppull = BeautifulSoup(html, "html.parser")
temp = httppull.find("div", class_ = "BNeawe").text
skystatus = httppull.find("div", class_ = 'BNeawe s3v9rd AP7Wnd').text
feelstatus = httppull.find("div", class_ = 'BNeawe tAd8D AP7Wnd').text

print(f"Tempature: {temp}")
print(f"Description: {skystatus}\n{feelstatus}")

### this is all i was able to do, im confused on how you take the classes directly from a website and put it in code, when ever i do that it just gives me "None" in the terminal ###