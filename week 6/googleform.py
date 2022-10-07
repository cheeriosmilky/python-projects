from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pyautogui as pg

web = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # opens google.
web.get('https://docs.google.com/forms/d/e/1FAIpQLScXNbdAs0HF9d5DHFXo1qTjK9wMSrG1nBCb1lzFw0tkJUGvOw/viewform')

pg.moveTo(2000,10)
pg.click()
pg.moveTo(2500,820)
pg.click()
pg.moveTo(2600,560)
pg.click()

time.sleep(500)


