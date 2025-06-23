import pytest
from selenium import webdriver
from pages.calc_page import CalculatorPage


@pytest.fixture
def driver():
    # Создание и закрытие браузера
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator_addition(driver):
    # Тест калькулятора через PageObject
    page = CalculatorPage(driver)
    page.open()
    page.set_delay(45)

    # Нажатие кнопок: 7 + 8 =
    for button in ['7', '+', '8', '=']:
        page.click_button(button)

    # Ожидание и проверка результата
    page.wait_for_result("15")
    assert page.get_result() == "15"
