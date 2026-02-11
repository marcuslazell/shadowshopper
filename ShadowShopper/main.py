import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FireFoxOptions

# This opens a new Firefox window
driver = webdriver.Firefox()

# This opens the testing website
driver.get("https://www.saucedemo.com")

# Visual Purposes
time.sleep(2)

# This block of code enters in the login credentials 
username = driver.find_element(By.ID, 'user-name')
username.send_keys("standard_user")
password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")

# Visual Purposes
time.sleep(1)

# Button Click
driver.find_element(By.ID, 'login-button').click()
if driver.current_url == 'https://www.saucedemo.com/inventory.html': {
    print ("Login Successful.")
}

# Stops the program
time.sleep(2)
driver.quit()