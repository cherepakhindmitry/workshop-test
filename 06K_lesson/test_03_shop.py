import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    yield driver
    driver.quit()


def test_shop_checkout_total(driver):
    # Открываем сайт магазина
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)

    # Авторизация
    wait.until(
        EC.presence_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Добавляем товары в корзину
    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
    )
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    # Переходим в корзину
    driver.find_element(
        By.CLASS_NAME, "shopping_cart_link"
    ).click()

    # Checkout
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
    wait.until(
        EC.presence_of_element_located((By.ID, "first-name"))
    ).send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    driver.find_element(By.ID, "continue").click()

    # Ожидаем страницу с итогами
    total_element = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total_text = total_element.text  # Пример: "Total: $58.29"

    # Выводим информацию
    print(f"Ожидаемая сумма: $58.29, Получено: {total_text}")

    # Проверка
    assert "$58.29" in total_text, (
        f"Ожидалось $58.29, но получили: {total_text}"
    )
