# Shadow Shopper 🛒
### Python Selenium Automation Framework

Shadow Shopper is an automated testing bot designed to validate the critical user flows of the SwagLabs e-commerce platform. It utilizes **Selenium WebDriver** and the **Page Object Model (POM)** design pattern to ensure robustness and scalability.

## 🚀 Key Features
* **Object-Oriented Design:** Encapsulated logic within a `ShadowShopper` class for modularity.
* **Dynamic Waits:** Replaced brittle `time.sleep()` calls with `WebDriverWait` and `ExpectedConditions` (EC) to handle network variability.
* **End-to-End Workflow:** Automates the entire user journey: Login -> Inventory Selection -> Cart Management -> Checkout -> Verification.
* **Self-Validating:** Includes internal assertions to verify "Order Complete" status automatically.

## 🛠 Technologies Used
* **Language:** Python 3.10+
* **Library:** Selenium WebDriver
* **Pattern:** Object-Oriented Programming (OOP)
* **Tools:** VS Code, Git

## 💻 How to Run
1.  Clone the repository:
    ```bash
    git clone [https://github.com/marcuslazell/shadowshopper.git](https://github.com/marcuslazell/shadowshopper.git)
    ```
2.  Install dependencies:
    ```bash
    pip install selenium
    ```
3.  Run the bot:
    ```bash
    python main.py
    ```

## 🔄 Recent Updates
* **Feb 2026:** Refactored from linear script to OOP Class structure.
* **Feb 2026:** Implemented Explicit Waits for element visibility.