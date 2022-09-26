from email import header
from wsgiref import headers
from bs4 import BeautifulSoup
import requests

url = 'https://weather.com/weather/today/l/b5898a548a77ef416b735bebad9f9a4458341248ee95bda165f9441aa82cb959'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
}

response = requests.get(url, headers = header)
soup = BeautifulSoup(response.content, 'lxml')

print(soup.select('.Feels Like')[1].get_text())