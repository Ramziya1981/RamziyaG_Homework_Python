from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.user_name = (By.ID, 'user-name')
        self.password = (By.ID, "password")
        self.login = (By.ID, "login-button")
        self.list = (By.CLASS_NAME, "inventory_list")
        
    def enter_username(self, username):
        username_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.user_name))
        username_field.send_keys(username)
        
    def enter_password(self, password):
        password_field =  WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.password))
        password_field.send_keys(password)
        
    def click_login(self):
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login))
        login_button.click()
        
    def is_login_successful(self):
        try:
            # Пример проверки: ищем элемент, который появляется только после успешной авторизации
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.list))
            return True
        except:
            return False
