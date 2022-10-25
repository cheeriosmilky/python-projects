from typing import Text
from bs4 import BeautifulSoup
import requests
#BNeawe iBp4i AP7Wnd

city = "Boardman Ohio"
url = "https://www.google.com/search?q="+"weather"+city
html = requests.get(url).content
httppull = BeautifulSoup(html, "html.parser")
temp = httppull.find("div", class_ = "BNeawe").text
tempstatus = httppull.find("div", class_ = 'BNeawe tAd8D AP7Wnd').text

info = tempstatus.split('\n')
skystatus = info[1]
templist = httppull.findAll("div", class_ = "Bneawe s3v9rd AP7Wnd")
divtags = templist[5]

wind = divtags.find("Wind")
data = divtags[wind:]

tempfeel = f"Tempature: {temp}"
skyfeel = f"Sky description: {skystatus}"

print(tempfeel)
print(skyfeel)

# i = 0
# for item in temp_list:
#     print(f"{i}: {item}")
#     i = i+1

# tempstatus = httppull.find_all("div")
# for item in tempstatus:
#     print(item)



#<div class="kCrYT"><div><div class="BNeawe s3v9rd AP7Wnd"><div><div><div class="BNeawe s3v9rd AP7Wnd">