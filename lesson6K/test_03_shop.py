from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка драйвера Firefox с явным ожиданием
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)  # ожидание до 10 секунд

try:
    # 1. Открыть сайт магазина
    driver.get("https://www.saucedemo.com/")

    # 2. Авторизация
    wait.until(EC.presence_of_element_located
               ((By.ID,
                 "user-name"
                 ))).send_keys("standard_user")
    wait.until(EC.presence_of_element_located
               ((By.ID, "password"))).send_keys("secret_sauce")
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

    # 3. Добавить товары в корзину
    products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for product in products:
        try:
            # Найти товар по названию и добавить в корзину
            product_button = wait.until(EC.element_to_be_clickable((
                By.XPATH, f"//div[text()='{product}']/ancestor::"
                "div[@class='inventory_item']//button"
            )))
            product_button.click()
        except NoSuchElementException:
            print(f"Товар {product} не найден!")
            continue

    # 4. Перейти в корзину
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME,
                                           "shopping_cart_link"))).click()

    # 5. Нажать Checkout
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    # 6. Заполнить форму
    wait.until(EC.presence_of_element_located((By.ID,
                                               "first-name"
                                               ))).send_keys("Ivan")
    wait.until(EC.presence_of_element_located((By.ID,
                                               "last-name"
                                               ))).send_keys("Ivanov")
    wait.until(EC.presence_of_element_located((By.ID,
                                               "postal-code"
                                               ))).send_keys("12345")

    # 7. Нажать Continue
    wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()

    # 8. Прочитать итоговую стоимость
    total_element = wait.until(EC.presence_of_element_located
                               ((By.CLASS_NAME, "summary_total_label")))
    total_text = total_element.text  # например, "Total: $58.29"
    total_amount = total_text.split("$")[1]

    print(f"Итоговая сумма: ${total_amount}")

    # Проверка суммы
    expected_total = "58.29"
    if total_amount == expected_total:
        print("Тест пройден: итоговая сумма совпадает с ожидаемой")
    else:
        print(f"Тест не пройден! Ожидалось: ${expected_total},"
              " получено: ${total_amount}")

except TimeoutException:
    print("Превышено время ожидания загрузки страницы")
except Exception as e:
    print(f"Произошла ошибка: {str(e)}")
finally:
    # Закрыть браузер
    driver.quit()
