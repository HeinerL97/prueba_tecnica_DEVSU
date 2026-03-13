from selenium.webdriver.common.by import By
import time

class CartPage:

    CART = (By.ID, "cartur")
    PLACE_ORDER = (By.XPATH, "//button[text()='Place Order']")

    def __init__(self, driver):
        self.driver = driver

    def open_cart(self):
        self.driver.find_element(*self.CART).click()
        time.sleep(2)

    def place_order(self):
        self.driver.find_element(*self.PLACE_ORDER).click()
        time.sleep(2)