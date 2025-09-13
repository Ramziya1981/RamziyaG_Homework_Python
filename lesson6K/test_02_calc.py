import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def test_calculator():
    """
    Автотест для калькулятора с задержкой
    """
    # Настройка Chrome WebDriver
    chrome_options = Options()
    # Максимальное окно браузера
    chrome_options.add_argument("--start-maximized")

    # Инициализация драйвера
    driver = webdriver.Chrome(options=chrome_options)

    # Шаг 1: Открыть страницу калькулятора
    print("Шаг 1: Открываю страницу калькулятора...")
    driver.get(
                "https://bonigarcia.dev/selenium"
                "-webdriver-java/slow-calculator.html"
        )

    # Шаг 2: Ввести значение 45 в поле задержки
    print("Шаг 2: Ввожу значение 45 в поле задержки...")
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("10")

    # Шаг 3: Нажать на кнопки 7, +, 8, =
    print("Шаг 3: Выполняю вычисление 7 + 8 = ...")

    # Нажимаем кнопку 7
    button_7 = driver.find_element(By.XPATH, "//span[text()='7']")
    button_7.click()

    # Нажимаем кнопку +
    button_plus = driver.find_element(By.XPATH, "//span[text()='+']")
    button_plus.click()

    # Нажимаем кнопку 8
    button_8 = driver.find_element(By.XPATH, "//span[text()='8']")
    button_8.click()

    # Нажимаем кнопку =
    button_equals = driver.find_element(By.XPATH, "//span[text()='=']")
    button_equals.click()

    # Шаг 4: Проверить результат 15 через 45 секунд
    print("Шаг 4: Ожидаю результат 15...")
    # Засекаем время начала операции
    start_time = time.time()

    # Ждем появления результата с таймаутом 50 секунд (чуть больше 45)
    wait = WebDriverWait(driver, 50)
    wait.until(
        EC.invisibility_of_element_located((By.ID, "spinner"))
    )

    # Получаем текст результата
    result_element = driver.find_element(By.CLASS_NAME, "screen")
    result_text = result_element.text

    # Засекаем время окончания операции
    end_time = time.time()
    # Вычисляем время выполнения
    execution_time = end_time - start_time

    # Проверяем результат
    assert result_text == "15", f"Ожидался результат '15', "\
        f"получен '{result_text}'"

    print(f"✅ Тест пройден успешно! Результат: {result_text}")

    # Проверяем, что время выполнения примерно соответствует
    # задержке (45 секунд)
    # Допускаем погрешность в ±5 секунд
    expected_delay = 10
    tolerance = 5
    if abs(execution_time - expected_delay) <= tolerance:
        print(f"✅ Время выполнения корректно: {execution_time:.2f}"
              " сек (ожидалось ~{expected_delay} сек)")

        
    else:
        print(f"⚠️ Время выполнения отличается от ожидаемого:"
              f" {execution_time:.2f} сек (ожидалось"
              f" ~{expected_delay} сек)")

    # Закрываем браузер
    print("Закрываю браузер...")
    driver.quit()


print("🚀 Запуск автотеста калькулятора...")
test_calculator()
print("🎉 Тест завершен!")
