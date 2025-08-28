from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    """Автотест для проверки валидации формы"""

    # Настройка Edge WebDriver
    edge_options = Options()
    edge_options.add_argument("--start-maximized")

    # Инициализация драйвера
    driver = webdriver.Edge(options=edge_options)

    try:
        # Шаг 1: Открыть страницу
        print("Шаг 1: Открываю страницу...")
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html",
            )

        # Ждем загрузки страницы
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "first-name"))
        )

        # Шаг 2: Заполнить форму
        print("Шаг 2: Заполняю форму...")

        # Заполнение полей формы
        driver.find_element(By.NAME, "first-name").send_keys("Иван")
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        # Шаг 3: Нажать кнопку Submit
        print("Шаг 3: Нажимаю кнопку Submit...")
        submit_button = driver.find_element(
            By.XPATH, "//button[@type='submit']"
            )
        submit_button.click()

        # Ждем загрузки страницы
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )

        # Шаг 4: Проверить, что поле Zip code подсвечено красным
        print("Шаг 4: Проверяю, что поле Zip code подсвечено красным...")
        zip_code_field = driver.find_element(By.ID, "zip-code")
        zip_code_classes = zip_code_field.get_attribute("class")

        # Проверяем наличие красного стиля
        # (обычно это класс alert py-2 alert-danger)
        assert "alert py-2 alert-danger" in zip_code_classes, "Поле Zip code "\
            "должно быть подсвечено красным, "\
            f"но имеет класс: {zip_code_classes}, "\
            "не являющийся красным"
        print("✓ Поле Zip code подсвечено красным")

        # Шаг 5: Проверить, что остальные поля подсвечены зеленым
        print("Шаг 5: Проверяю, что остальные поля подсвечены зеленым...")

        # Список полей для проверки (исключая Zip code)
        fields_to_check = [
            "first-name",
            "last-name",
            "address",
            "e-mail",
            "phone",
            "city",
            "country",
            "job-position",
            "company"
        ]

        for field_id in fields_to_check:
            field = driver.find_element(By.ID, field_id)
            field_classes = field.get_attribute("class")

            # Проверяем наличие зеленого стиля (обычно это класс is-valid)
            assert "alert py-2 alert-success" in field_classes, "Поле"\
                f" {field_id} должно быть подсвечено зеленым, но имеет"\
                f" класс: {field_classes}, не являющийся зелёным"
            print(f"✓ Поле {field_id} подсвечено зеленым")

        print("\n🎉 Все проверки пройдены успешно!")

    except Exception as e:
        print(f"❌ Ошибка во время выполнения теста: {e}")
        raise
    finally:
        # Закрыть браузер
        print("Закрываю браузер...")
        driver.quit()


if __name__ == "__main__":
    test_form_validation()
