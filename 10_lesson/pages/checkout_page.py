from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы оформления заказа.

        :param driver: Экземпляр веб-драйвера.
        """
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")

    def fill_form(self, first: str, last: str, zip_code: str) -> None:
        """
        Заполняет форму оформления заказа.

        :param first: Имя.
        :param last: Фамилия.
        :param zip_code: Почтовый индекс.
        :return: None
        """
        self.driver.find_element(*self.first_name).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.postal_code).send_keys(zip_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total(self) -> str:
        """
        Получает итоговую сумму заказа.

        :return: Строка с текстом общей суммы.
        """
        total_element = self.driver.find_element(
            By.CLASS_NAME, "summary_total_label"
        )
        return total_element.text
