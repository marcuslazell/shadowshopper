from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FireFoxOptions

# This opens a new Firefox window
driver = webdriver.Firefox()

driver.get("https://www.google.com")

import time
time.sleep(5)
driver.quit()