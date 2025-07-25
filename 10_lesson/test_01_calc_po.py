import pytest
import allure
from selenium import webdriver
from pages.calc_page import CalculatorPage


@pytest.fixture
def driver() -> webdriver.Chrome:
    """Фикстура для запуска и завершения браузера Chrome."""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.title("Проверка сложения 7 + 8 = 15")
@allure.description("Тест проверяет корректность операции сложения"
                    " в калькуляторе через PageObject")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_addition(driver: webdriver.Chrome) -> None:
    """Тест: ввод 7 + 8 и проверка, что результат равен 15."""
    page = CalculatorPage(driver)

    with allure.step("Открыть калькулятор и установить задержку"):
        page.open()
        page.set_delay(45)

    with allure.step("Нажать кнопки 7 + 8 ="):
        for button in ['7', '+', '8', '=']:
            page.click_button(button)

    with allure.step("Ожидание и проверка результата"):
        page.wait_for_result("15")
        assert page.get_result() == "15"
