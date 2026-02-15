from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FireFoxOptions

class ShadowShopper:

    # Enviroment Setup
    def __init__(self):
        # This will run automatically when the bot is created
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.saucedemo.com")

    # Modular Login Logic
    def login(self, user, password):
        self.wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(user)
        self.wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(password)
        self.driver.find_element(By.ID, 'login-button').click()
        self.wait.until(EC.url_to_be('https://www.saucedemo.com/inventory.html'))
        print ("Login Successful.")

    # Adds Backpack to Shopping Cart and Opens Shoping Cart Page
    def add_backpack_to_cart (self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
        print("Backpack added to cart")
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_badge"))).click()
        print("Shopping cart has been open")
        self.wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    # Check out with parameters
    def checkout(self, first_name, last_name, zip_code):
        self.wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys(first_name)
        self.wait.until(EC.visibility_of_element_located((By.ID, "last-name"))).send_keys(last_name)
        self.wait.until(EC.visibility_of_element_located((By.ID, "postal-code"))).send_keys(zip_code)
        self.wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()
        self.wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

    # Quits Script
    def teardown(self):
        self.driver.quit()

    def verify_order(self):
        try:
            # Wait for the success message
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
            
            # Grab the text to be double sure
            success_text = self.driver.find_element(By.CLASS_NAME, "complete-header").text
            
            # Verify the text matches exactly
            if "Thank you for your order!" in success_text:
                print("TEST PASSED: Order Complete!")
            else:
                print(f"TEST FAILED: Text mismatch. Found: {success_text}")

        except:
            # If the wait times out (element never appeared)
            print("TEST FAILED: Success message never appeared.")

# The "Main" Execution Block
if __name__ == "__main__":
        bot = ShadowShopper()
        bot.login("standard_user", "secret_sauce")
        bot.add_backpack_to_cart()
        bot.checkout("Marc", "Shaw", "91325")
        bot.verify_order()
        bot.teardown()
    