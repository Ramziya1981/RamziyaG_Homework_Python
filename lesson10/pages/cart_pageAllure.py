from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class  CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.selector = (By.CSS_SELECTOR, "#checkout")
    
    def click_checkout(self):
        checkout_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.selector))
        checkout_button.click()