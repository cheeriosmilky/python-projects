from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from logging.config import fileConfig
from bs4 import BeautifulSoup
import requests

fnameask = input('fname: ')
mnameask = input('mname: ')
lnameask = input('lname: ')
byearask = input('byear: ')
dyearask = input('dyear: ')
locask = input('loc: ')



web = f'https://www.findagrave.com/memorial/search?firstname={fnameask}&middlename={mnameask}&lastname={lnameask}&birthyear={byearask}&birthyearfilter=&deathyear={dyearask}&deathyearfilter=&location={locask}&locationId=&memorialid=&mcid=&linkedToName=&datefilter=&orderby=r&plot='
html = requests.get(web).content
httppull = BeautifulSoup(html, 'html.parser')

p1 = httppull.find('div', class_='name-grave')
p1.click()




