from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver: WebDriver, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait

    @allure.step("Поиск элемента по локатору")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    @allure.step("Проверка наличия элемента")
    def is_element_present(self, locator) -> bool:
        try:
            self.find_element(locator)
            return True
        except:
            return False

    @allure.step("Ожидание исчезновения элемента")
    def wait_for_element_disappear(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))