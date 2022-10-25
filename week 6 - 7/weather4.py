from bs4 import BeautifulSoup
import requests
#BNeawe iBp4i AP7Wnd

def search():
    google = 'Weather in {Boardman Youngstown Ohio}'
    url = (f"https://www.google.com/search?&q={google}")
    request = requests.get(url)
    httppull = BeautifulSoup(request.text, "html.parser")
    # tempature = httppull.find('div', attrs={'class': 'gNCp2e'})
    # print(httppull)
    # tempstatus = httppull.find_all("span", class_ = 'wob_t')
    # tempstatus = httppull.find_all("div", attrs={'class' : 'BNeawe s3v9rd AP7Wnd'})
    tempstatus = httppull.find("div", attrs={'class' : 'BNeawe s3v9rd AP7Wnd'})
    # tempstatus = httppull.find_all("div", attrs={'class' : 'wob_t'})
    temp_list = tempstatus.text.split('\n')
    print(temp_list)

    i = 0
    for item in temp_list:
        print(f"{i}: {item}")
        i = i+1



    # tempstatus = httppull.find_all("div")
    # for item in tempstatus:
    #     print(item)
search()


#<div class="kCrYT"><div><div class="BNeawe s3v9rd AP7Wnd"><div><div><div class="BNeawe s3v9rd AP7Wnd">