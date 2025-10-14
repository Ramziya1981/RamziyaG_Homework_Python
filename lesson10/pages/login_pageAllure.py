import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, ".error")
    
    @allure.step("Ввод имени пользователя")
    def enter_username(self, username):
       with allure.step(f"Вводим имя пользователя: {username}"):
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(self.username_field)
            ).send_keys(username)


    @allure.step("Ввод пароля")
    def enter_password(self, password):
        with allure.step(f"Вводим пароль: {password}"):
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(self.password_field)
            ).send_keys(password)


    @allure.step("Нажать кнопку входа")
    def click_login(self):
        with allure.step("Нажимаем кнопку входа"):
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.login_button)
            ).click()
    

    @allure.step("Проверка успешного входа")
    def is_login_successful(self):
        try:
            with allure.step("Проверяем наличие контейнера инвентаря"):
                WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".inventory_container"))
                )
                return True
        except Exception as e:
            allure.attach(str(e), name="Ошибка при проверке", attachment_type=allure.attachment_type.TEXT)
            return False
  