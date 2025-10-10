from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class MainPage:
    def __init__(self, driver):  
        self.driver = driver
         # Обновленные локаторы
        self.cart_button = (By.CSS_SELECTOR, "#shopping_cart_container button")
        # Другие локаторы...

    def add_product_to_cart(self, product_name):
        # Реализация метода с учетом новых локаторов
        pass

    def go_to_cart(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.cart_button)
        ).click()