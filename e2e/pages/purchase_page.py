from selenium.webdriver.common.by import By
import time


class PurchasePage:

    NAME = (By.ID, "name")
    COUNTRY = (By.ID, "country")
    CITY = (By.ID, "city")
    CARD = (By.ID, "card")
    MONTH = (By.ID, "month")
    YEAR = (By.ID, "year")
    PURCHASE = (By.XPATH, "//button[text()='Purchase']")

    def __init__(self, driver):
        self.driver = driver

    def confirm_purchase(self):

        self.driver.find_element(*self.NAME).send_keys("Test User")
        self.driver.find_element(*self.COUNTRY).send_keys("Colombia")
        self.driver.find_element(*self.CITY).send_keys("Bogota")
        self.driver.find_element(*self.CARD).send_keys("123456789")
        self.driver.find_element(*self.MONTH).send_keys("06")
        self.driver.find_element(*self.YEAR).send_keys("2026")

        time.sleep(1)

        self.driver.find_element(*self.PURCHASE).click()