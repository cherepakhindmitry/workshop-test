from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    """PageObject для работы со страницей калькулятора."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация элементов страницы калькулятора.

        :param driver: Экземпляр драйвера Selenium
        """
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.result = (By.CSS_SELECTOR, ".screen")

    def open(self) -> None:
        """Открывает страницу калькулятора."""
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def set_delay(self, value: int) -> None:
        """
        Устанавливает задержку выполнения калькулятора.

        :param value: Задержка в секундах
        """
        self.driver.find_element(*self.delay_input).clear()
        self.driver.find_element(*self.delay_input).send_keys(str(value))

    def click_button(self, label: str) -> None:
        """
        Нажимает кнопку на калькуляторе по её тексту.

        :param label: Текст на кнопке (например, '7', '+', '=')
        """
        button = self.driver.find_element(
            By.XPATH, f"//span[text()='{label}']"
        )
        button.click()

    def wait_for_result(self, expected: str, timeout: int = 50) -> None:
        """
        Ожидает появления результата на экране.

        :param expected: Ожидаемый текст результата
        :param timeout: Максимальное время ожидания (по умолчанию 50 секунд)
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.result, expected)
        )

    def get_result(self) -> str:
        """
        Получает текст результата с экрана калькулятора.

        :return: Результат, отображаемый на экране
        """
        return self.driver.find_element(*self.result).text
