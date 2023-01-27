from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

from logging.config import fileConfig
from bs4 import BeautifulSoup
import requests

fnameask = input('fname: ')
mnameask = input('mname: ')
lnameask = input('lname: ')
byearask = input('byear: ')
dyearask = input('dyear: ')
locask = input('loc: ')

op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op, service=Service(ChromeDriverManager().install()))
driver.get(f'https://www.findagrave.com/memorial/search?firstname={fnameask}&middlename={mnameask}&lastname={lnameask}&birthyear={byearask}&birthyearfilter=&deathyear={dyearask}&deathyearfilter=&location={locask}&locationId=&memorialid=&mcid=&linkedToName=&datefilter=&orderby=r&plot=')
ogclick = driver.find_elements(By.CLASS_NAME, 'name-grave')[0]
ogclick.click()
bday = driver.find_element(By.ID, 'birthDateLabel')
dday = driver.find_element(By.ID, 'deathDateLabel')
burial = driver.find_elements(By.CLASS_NAME, 'col-8')[2]
print(f'----------> {burial.text}')

# html = requests.get(web).content
# httppull = BeautifulSoup(html, 'html.parser')

# p1 = httppull.find('div', class_='name-grave')
# p1.send_keys({fnameask})



