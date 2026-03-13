from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:

    ADD_TO_CART = (By.LINK_TEXT, "Add to cart")
    HOME = (By.ID, "nava")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_product(self):

        add_btn = self.wait.until(
            EC.element_to_be_clickable(self.ADD_TO_CART)
        )
        add_btn.click()

        alert = self.wait.until(EC.alert_is_present())
        alert.accept()

    def return_home(self):

        home = self.wait.until(
            EC.element_to_be_clickable(self.HOME)
        )
        home.click()