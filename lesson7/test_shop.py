import pytest
from selenium import webdriver


from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


def test_shop(driver):
    # Авторизация
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Проверка успешной авторизации
    assert login_page.is_login_successful(), "Авторизация не прошла успешно"

    # Работа с главной страницей
    main_page = MainPage(driver)
    products = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]

    for product in products:
        main_page.add_product_to_cart(product)

    main_page.go_to_cart()

    # Работа с корзиной
    cart_page = CartPage(driver)
    cart_page.click_checkout()

    # Работа с оформлением заказа
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Иван", "Иванов", "12345")
    checkout_page.click_continue()

    # Получение итоговой суммы
    total_amount = checkout_page.get_total_amount()

    # Проверка итоговой суммы
    expected_total = "58.29"
    assert total_amount == expected_total, (
        f"Ожидалось: {expected_total}, "
        f"получено: {total_amount}"
    )
    print(
        f"Тест пройден: итоговая сумма {total_amount}"
        f"совпадает с ожидаемой"
    )
