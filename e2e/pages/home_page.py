from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    PHONE = (By.LINK_TEXT, "Samsung galaxy s6")
    LAPTOP = (By.LINK_TEXT, "Sony vaio i5")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def select_phone(self):
        phone = self.wait.until(
            EC.element_to_be_clickable(self.PHONE)
        )
        phone.click()

    def select_laptop(self):
        laptop = self.wait.until(
            EC.element_to_be_clickable(self.LAPTOP)
        )
        laptop.click()