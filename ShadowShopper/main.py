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
backpack_btn = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
backpack_btn.click()
print("Backpack added to cart")

# Get to the checkout out screen
shopping_cart = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_badge")))
shopping_cart.click()
print("Shopping cart has been open")
check_out = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
check_out.click()

# Checkingout
first_name = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
first_name.send_keys("Marc")
last_name = wait.until(EC.visibility_of_element_located((By.ID, "last-name")))
last_name.send_keys("Shaw")
postal_code = wait.until(EC.visibility_of_element_located((By.ID, "postal-code")))
postal_code.send_keys("91210")

continue_button = wait.until(EC.element_to_be_clickable((By.ID, "continue")))
continue_button.click()

finish_button = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
finish_button.click()

try:
    # Wait for the success message
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
    
    # Grab the text to be double sure
    success_text = driver.find_element(By.CLASS_NAME, "complete-header").text
    
    # Verify the text matches exactly
    if "Thank you for your order!" in success_text:
        print("TEST PASSED: Order Complete!")
    else:
        print(f"TEST FAILED: Text mismatch. Found: {success_text}")

except:
    # If the wait times out (element never appeared)
    print("TEST FAILED: Success message never appeared.")

# Stops the program
driver.quit()