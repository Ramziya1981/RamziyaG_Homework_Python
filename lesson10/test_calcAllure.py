import pytest
import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


# Класс страницы калькулятора
class CalculatorPage:
    def __init__(self, driver: webdriver.Chrome):
        """
        Инициализация страницы калькулятора
        :param driver: экземпляр веб-драйвера
        """
        self.driver = driver
        self.delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        self.screen = driver.find_element(By.CLASS_NAME, "screen")
        self.spinner = driver.find_element(By.ID, "spinner")

    def set_delay(self, delay: int) -> None:
        """
        Установка значения задержки
        :param delay: значение задержки в секундах
        """
        self.delay_input.clear()
        self.delay_input.send_keys(str(delay))

    def click_button(self, button_text: str) -> None:
        """
        Нажатие на кнопку калькулятора
        :param button_text: текст кнопки для нажатия
        """
        button = self.driver.find_element(
            By.XPATH,
            f"//span[text()='{button_text}']"
        )
        button.click()

    def get_result(self) -> str:
        """
        Получение результата вычисления
        :return: текст результата
        """
        return self.screen.text

    def wait_for_calculation(self) -> None:
        """
        Ожидание завершения вычисления
        """
        WebDriverWait(self.driver, 50).until(
            EC.invisibility_of_element_located((By.ID, "spinner"))
        )


# Фикстура для управления веб-драйвером
@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@allure.feature("Калькулятор")
@allure.story("Проверка базового вычисления")
@allure.title("Тест сложения двух чисел")
@allure.description("Проверка корректности сложения чисел с учетом задержки")
@allure.severity(allure.severity_level.BLOCKER)
def test_calculator(browser):
    with allure.step("Открываю страницу калькулятора"):
        browser.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    calculator = CalculatorPage(browser)

    with allure.step("Ввожу значение задержки"):
        calculator.set_delay(5)

    with allure.step("Выполняю вычисление 7 + 8"):
        calculator.click_button("7")
        calculator.click_button("+")
        calculator.click_button("8")
        calculator.click_button("=")

    with allure.step("Ожидаю результат"):
        start_time = time.time()
        calculator.wait_for_calculation()
        end_time = time.time()

    @allure.step("Проверяю результат вычисления")
    def check_result():
        result = calculator.get_result()
        assert result == "15", f"Ожидался результат '15', получен '{result}'"
    check_result()

    @allure.step("Проверяю время выполнения")
    def check_execution_time():
        execution_time = end_time - start_time
        expected_delay = 5
        tolerance = 5
        assert abs(execution_time - expected_delay) <= tolerance, (
            f"Время выполнения отличается от ожидаемого: "
            f"{execution_time:.2f} сек (ожидалось ~{expected_delay} сек)"
        )
    check_execution_time()
