from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        # Локаторы элементов
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_amount = (By.CSS_SELECTOR, "#total-cart-value")

    def fill_form(self, first_name, last_name, postal_code):
         # Добавляем проверку видимости элементов
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.first_name)
        ).send_keys(last_name)
        
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.last_name)
        ).send_keys(last_name)
        
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.postal_code)
        ).send_keys(postal_code)

    def click_continue(self):
        # Нажимаем кнопку Continue
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.continue_button)
        ).click()

    def get_total_amount(self):
        # Получаем итоговую сумму
        total = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.total_amount)
        ).text
        return total.replace("$", "")  # Убираем символ валюты
        
