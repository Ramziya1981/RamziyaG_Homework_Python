from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.selector2  = (By.CSS_SELECTOR, "#shopping_cart_container a")
    
    def add_product_to_cart(self, product_name):
        # Добавляем ожидание полной загрузки страницы
        #WebDriverWait(self.driver, 100).until(EC.title_is(product_name))
        product =  WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((
            By.XPATH, f"//div[text()='{product_name}']/ancestor::"
            "div[@class='inventory_item']//button"
            )))
        product.click()
    
    def go_to_cart(self):
        cart_button =  WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.selector2))
        cart_button.click()