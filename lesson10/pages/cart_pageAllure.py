from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        # Обновленные локаторы
        self.checkout_button = (By.CSS_SELECTOR, "#checkout")
    
    
    @allure.step("Нажать кнопку входа")
    def click_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()



