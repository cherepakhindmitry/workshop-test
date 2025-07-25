import pytest
import allure
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver() -> webdriver.Firefox:
    """Фикстура для запуска и завершения браузера Firefox."""
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@allure.title("Проверка оформления заказа")
@allure.description("Добавление товаров в корзину и прохождение"
                    "оформления заказа до получения суммы")
@allure.feature("Магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_checkout(driver: webdriver.Firefox) -> None:
    """Тест: добавление товаров и оформление заказа, проверка суммы."""
    with allure.step("Открыть страницу логина и авторизоваться"):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавить товары в корзину и перейти в корзину"):
        inventory = InventoryPage(driver)
        inventory.add_to_cart("Sauce Labs Backpack")
        inventory.add_to_cart("Sauce Labs Bolt T-Shirt")
        inventory.add_to_cart("Sauce Labs Onesie")
        inventory.go_to_cart()

    with allure.step("Перейти к оформлению заказа"):
        cart = CartPage(driver)
        cart.click_checkout()

    with allure.step("Заполнить форму оформления и получить итоговую сумму"):
        checkout = CheckoutPage(driver)
        checkout.fill_form("Иван", "Иванов", "123456")
        total = checkout.get_total()

    with allure.step("Проверить, что итоговая сумма корректна"):
        assert total == "Total: $58.29"
