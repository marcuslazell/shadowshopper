from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FireFoxOptions

# This opens a new Firefox window
driver = webdriver.Firefox()

# This opens the testing website
driver.get("https://www.saucedemo.com")

# For Visual Purposes & Slower internet connections
wait = WebDriverWait(driver, 10)

# This block of code enters in the login credentials 
username = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
username.send_keys("standard_user")
password = wait.until(EC.visibility_of_element_located((By.ID, "password")))
password.send_keys("secret_sauce")

# Button Click 
driver.find_element(By.ID, 'login-button').click()

wait.until(EC.url_to_be('https://www.saucedemo.com/inventory.html'))
print ("Login Successful.")
driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
print ("Backpack added to cart")

# Stops the program
driver.quit()