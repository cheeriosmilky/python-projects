from bs4 import BeautifulSoup
import requests
#BNeawe iBp4i AP7Wnd

def search():
    # google = 'Weather in {Boardman Youngstown Ohio}'
    url = (f"https://www.wunderground.com/forecast/us/oh/boardman")
    request = requests.get(url)
    httppull = BeautifulSoup(request.text, "html.parser")
    tempature = httppull.find('span', attrs={'class': 'temp-hi'})
    print(tempature)