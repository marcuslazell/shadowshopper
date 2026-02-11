from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FireFoxOptions

# This opens a new Firefox window
driver = webdriver.Firefox()

driver.get("https://www.saucedemo.com")

username = driver.find_element(By.ID, 'user-name')
username.send_keys("standard_user")
password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")

import time
time.sleep(5)
driver.quit()