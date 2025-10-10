import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import Severity
import allure


from pages.login_pageAllure import LoginPage
from pages.main_pageAllure import MainPage
from pages.cart_pageAllure import CartPage
from pages.checkout_pageAllure import CheckoutPage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


@allure.feature("Покупка товаров")
@allure.story("Полный цикл покупки")
@allure.title("Тестирование процесса покупки товаров")
@allure.description("Тест проверяет весь процесс покупки: "
                   "авторизацию, добавление товаров в корзину, "
                   "оформление заказа и проверку итоговой суммы")
@allure.severity(Severity.CRITICAL)


def test_shop(driver):
    # Авторизация
    login_page = LoginPage(driver)
    with allure.step("Авторизация пользователя"):
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

    with allure.step("Проверка успешной авторизации"):
        assert login_page.is_login_successful(), "Авторизация не прошла успешно"

    # Работа с главной страницей
    main_page = MainPage(driver)
    products = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]

    with allure.step("Добавление товаров в корзину"):
        for product in products:
            main_page.add_product_to_cart(product)
    
    with allure.step("Переход в корзину"):
        main_page.go_to_cart()
    
    # Работа с корзиной
    cart_page = CartPage(driver)
    
    with allure.step("Переход к оформлению заказа"):
        cart_page.click_checkout()
    
    # Работа с оформлением заказа
    checkout_page = CheckoutPage(driver)
    
    with allure.step("Заполнение формы заказа"):
        checkout_page.fill_form("Иван", "Иванов", "12345")
        checkout_page.click_continue()
    
    # Получение итоговой суммы
    with allure.step("Получение итоговой суммы"):
        total_amount = checkout_page.get_total_amount()
    
    with allure.step("Проверка итоговой суммы"):
        expected_total = "58.29"
        assert total_amount == expected_total, (
            f"Ожидалось: {expected_total}, "
            f"получено: {total_amount}"
        )
        allure.attach(f"Тест пройден: итоговая сумма {total_amount} "
                     f"совпадает с ожидаемой")
