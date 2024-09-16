from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DemoBlazeAutomation:
    def __init__(self, driver):
        self.driver = driver

    def open_website(self):
        self.driver.get("https://www.demoblaze.com/index.html")
        time.sleep(2)

    def login(self, username, password):
        login_btn = self.driver.find_element(By.XPATH, '//*[@id="login2"]')
        login_btn.click()
        time.sleep(3)

        username_input = self.driver.find_element(By.XPATH, '//*[@id="loginusername"]')
        username_input.send_keys(username)

        password_input = self.driver.find_element(By.XPATH, '//*[@id="loginpassword"]')
        password_input.send_keys(password)

        login_submit_btn = self.driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
        login_submit_btn.click()
        time.sleep(2)

    def logout(self):
        user_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'nameofuser'))
        )
        user_dropdown.click()

        logout_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'logout2'))
        )
        logout_btn.click()

    def navigate_to_category(self, category_name):
        category_link = self.driver.find_element(By.XPATH, f'//a[text()="{category_name}"]')
        category_link.click()

    def add_product_to_cart(self, product_name):
        product_xpath = f'//a[text()="{product_name}"]'
        wait = WebDriverWait(self.driver, 10)

        # Wait for the product link to be clickable
        product_link = wait.until(EC.element_to_be_clickable((By.XPATH, product_xpath)))
        product_link.click()

        # Wait for the 'Add to Cart' button to be clickable
        add_to_cart_btn_xpath = '//a[contains(@class, "btn-success") and contains(@onclick, "addToCart")]'
        wait.until(EC.element_to_be_clickable((By.XPATH, add_to_cart_btn_xpath)))

        add_to_cart_btn = self.driver.find_element(By.XPATH, add_to_cart_btn_xpath)
        add_to_cart_btn.click()

    def go_to_cart(self):
        cart_link = self.driver.find_element(By.XPATH, '//*[@id="cartur"]')
        cart_link.click()

    def close_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
