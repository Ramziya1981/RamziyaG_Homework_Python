from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.selector1 = (By.ID, "first-name")
        self.selector2 = (By.ID, "last-name")
        self.selector3 = (By.ID, "postal-code")
        self.selector4 = (By.CSS_SELECTOR, "#continue")
        self.selector5 = (By.CLASS_NAME, "summary_total_label")

    
    def fill_form(self, first_name, last_name, postal_code):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.selector1)).send_keys(first_name)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.selector2)).send_keys(last_name)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.selector3)).send_keys(postal_code)
    
    def click_continue(self):
        continue_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.selector4))
        continue_button.click()
    
    def get_total_amount(self):
        total_amount = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.selector5))
        return total_amount.text.split("$")[1]