import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


# Класс страницы калькулятора
class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        self.screen = driver.find_element(By.CLASS_NAME, "screen")
        self.spinner = driver.find_element(By.ID, "spinner")

    def set_delay(self, delay):
        self.delay_input.clear()
        self.delay_input.send_keys(str(delay))

    def click_button(self, button_text):
        button = self.driver.find_element(
            By.XPATH,
            f"//span[text()='{button_text}']"
        )
        button.click()

    def get_result(self):
        return self.screen.text

    def wait_for_calculation(self):
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


def test_calculator(browser):
    # Открыть страницу калькулятора
    print("Шаг 1: Открываю страницу калькулятора...")
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    # Инициализация страницы калькулятора
    calculator = CalculatorPage(browser)

    # Устанавливаем задержку
    print("Шаг 2: Ввожу значение 45 в поле задержки...")
    calculator.set_delay(45)

    # Выполнить вычисление
    print("Шаг 3: Выполняю вычисление 7 + 8 = ...")
    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    calculator.click_button("=")

    # Дождаться результата
    print("Шаг 4: Ожидаю результат 15...")
    start_time = time.time()
    calculator.wait_for_calculation()
    end_time = time.time()

    # Проверка результата
    result = calculator.get_result()
    assert result == "15", f"Ожидался результат '15', получен '{result}'"
    print(f"✅ Тест пройден успешно! Результат: {result}")

    # Проверка времени выполнения
    execution_time = end_time - start_time
    expected_delay = 45
    tolerance = 5
    assert abs(execution_time - expected_delay) <= tolerance, (
        f"Время выполнения отличается от ожидаемого: "
        f"{execution_time:.2f} сек (ожидалось ~{expected_delay} сек)"
    )
    print(
        f"✅ Время выполнения корректно: "
        f"{execution_time:.2f} сек (ожидалось ~{expected_delay} сек)"
    )
