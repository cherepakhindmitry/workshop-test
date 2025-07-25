from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """Класс для взаимодействия со страницей корзины."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует элементы страницы корзины.

        :param driver: экземпляр Selenium WebDriver
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    def click_checkout(self) -> None:
        """
        Нажимает на кнопку оформления заказа (Checkout).
        """
        self.driver.find_element(*self.checkout_button).click()
