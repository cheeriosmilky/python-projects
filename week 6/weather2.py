from bs4 import BeautifulSoup
import requests
#BNeawe iBp4i AP7Wnd

def search():
    # # google = 'Weather in {Boardman Youngstown Ohio}'
    # url = (f"https://www.wunderground.com/forecast/us/oh/boardman")
    # request = requests.get(url)
    # httppull = BeautifulSoup(request.text, "html.parser")
    # tempature = httppull.find('span', attrs={'class': 'temp-hi'})
    # print(tempature)

    city = "Boardman Ohio"
    url = "https://www.google.com/search?q="+"weather"+city
    html = requests.get(url).content
    httppull = BeautifulSoup(html, "html.parser")
    temp = httppull.find("div", class_ = "BNeawe").text
    tempstatus = httppull.find("div", class_ = 'BNeawe tAd8D AP7Wnd').text
    print(tempstatus)
search()