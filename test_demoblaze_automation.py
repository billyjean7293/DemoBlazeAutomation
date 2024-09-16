import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from demoblaze_automation import DemoBlazeAutomation


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.usefixtures("driver")
class TestDemoBlazeAutomation:
    def test_open_website(self, driver):
        automation = DemoBlazeAutomation(driver)
        automation.open_website()
        time.sleep(2)
        assert driver.current_url == "https://www.demoblaze.com/index.html"


    def test_login(self, driver):
        automation = DemoBlazeAutomation(driver)
        automation.open_website()
        time.sleep(2)
        username = "moneymike123"
        password = "moneymike123"
        automation.login(username, password)
        time.sleep(3)
        user_link = driver.find_element(By.ID, "nameofuser")
        time.sleep(3)
        assert user_link.text == f"Welcome {username}"
        automation.logout()



    def test_logout(self, driver):
        automation = DemoBlazeAutomation(driver)
        automation.open_website()
        time.sleep(2)
        automation.login("moneymike123", "moneymike123")
        automation.logout()
        time.sleep(3)
        login_btn = driver.find_element(By.ID, "login2")
        time.sleep(3)
        assert login_btn.is_displayed()


    def test_navigate_to_category(self, driver):
        automation = DemoBlazeAutomation(driver)
        automation.open_website()
        automation.navigate_to_category("Laptops")
        time.sleep(3)
        automation.navigate_to_category("Phones")
        time.sleep(2)
        category_header = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a')
        assert category_header.text == "Samsung galaxy s6"

    def test_go_to_cart(self, driver):
        automation = DemoBlazeAutomation(driver)
        automation.open_website()

        automation.go_to_cart()

        wait = WebDriverWait(driver, 10)
        cart_header = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div/div[1]/h2')))
        assert cart_header.text == "Products"


    def test_add_product_to_cart(self, driver):
        automation = DemoBlazeAutomation(driver)
        automation.open_website()

        automation.navigate_to_category("Phones")
        automation.add_product_to_cart("Samsung galaxy s6")

        automation.close_alert()

        automation.go_to_cart()

        time.sleep(3)

        product_in_cart = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/table/tbody/tr/td[2]')
        assert product_in_cart.is_displayed()

    def test_remove_product_from_cart(self, driver):
        automation = DemoBlazeAutomation(driver)
        automation.open_website()

        automation.navigate_to_category("Phones")
        automation.add_product_to_cart("Samsung galaxy s6")

        automation.close_alert()

        automation.go_to_cart()
        time.sleep(2)
        # This is code is ran individually
        # delete_btn1 = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/table/tbody/tr/td[4]/a')
        # delete_btn1.click()

        delete_btn1 = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/table/tbody/tr[1]/td[4]/a')
        delete_btn1.click()

        time.sleep(2)

        delete_btn2 = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/table/tbody/tr/td[4]/a')
        delete_btn2.click()

        time.sleep(2)

        with pytest.raises(Exception):
            driver.find_element(By.XPATH, '//td[text()="Samsung galaxy s6"]')


    def test_complete_purchase(self, driver):
        automation = DemoBlazeAutomation(driver)
        automation.open_website()

        automation.navigate_to_category("Phones")
        automation.add_product_to_cart("Samsung galaxy s6")

        automation.close_alert()

        automation.go_to_cart()

        place_order_btn = driver.find_element(By.XPATH, '//html/body/div[6]/div/div[2]/button')
        place_order_btn.click()

        time.sleep(2)

        # Fill in the purchase form here
        name_input = driver.find_element(By.ID, "name")
        name_input.send_keys("John Doe")

        time.sleep(2)

        country_input = driver.find_element(By.ID, "country")
        country_input.send_keys("United States")

        time.sleep(2)

        city_input = driver.find_element(By.ID, "city")
        city_input.send_keys("Fort Myers")

        time.sleep(2)

        credit_card_input = driver.find_element(By.ID, "card")
        credit_card_input.send_keys("1234567890")

        time.sleep(2)

        month_input = driver.find_element(By.ID, "month")
        month_input.send_keys("July")

        time.sleep(2)

        year_input = driver.find_element(By.ID, "year")
        year_input.send_keys("2000")

        time.sleep(2)

        purchase_btn = driver.find_element(By.XPATH, '//button[text()="Purchase"]')
        purchase_btn.click()
        time.sleep(4)
        success_msg = driver.find_element(By.XPATH, '//h2[text()="Thank you for your purchase!"]')
        assert success_msg.is_displayed()
