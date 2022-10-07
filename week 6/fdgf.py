from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

web = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # opens google.
web.get('https://docs.google.com/forms/d/e/1FAIpQLScXNbdAs0HF9d5DHFXo1qTjK9wMSrG1nBCb1lzFw0tkJUGvOw/viewform')
time.sleep(5000)
l = web.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
l.send_keys("Factor_Jon@student.mahoningctc.com")
l.send_keys(Keys.RETURN)
time.sleep(5000)