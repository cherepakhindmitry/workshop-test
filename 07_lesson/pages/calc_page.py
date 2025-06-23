from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.ID, "delay")  # Поле ввода задержки
        self.result = (By.CSS_SELECTOR, ".screen")  # Поле с результатом

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def set_delay(self, value):
        self.driver.find_element(*self.delay_input).clear()
        self.driver.find_element(*self.delay_input).send_keys(str(value))

    def click_button(self, label):
        # Нажатие на кнопку по тексту
        button = self.driver.find_element(
            By.XPATH, f"//span[text()='{label}']"
        )
        button.click()

    def wait_for_result(self, expected, timeout=50):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.result, expected)
        )

    def get_result(self):
        return self.driver.find_element(*self.result).text
