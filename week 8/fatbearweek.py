from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import pyautogui as pg

options = Options()
options.headless = True
options.add_argument('--headless')
incognito = Options()
incognito.add_argument('--incognito')
i=0
# web = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=incognito) # opens google.
# web.get('https://explore.org/fat-bear-week')
# time.sleep(500)
pg.moveTo(500,500)