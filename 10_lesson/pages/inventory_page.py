from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class InventoryPage:
    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор страницы списка товаров.

        :param driver: Экземпляр веб-драйвера Selenium.
        """
        self.driver = driver

    def add_to_cart(self, product_name: str) -> None:
        """
        Добавляет товар в корзину по его названию.

        :param product_name: Название товара, отображаемое на странице.
        """
        locator = (
            By.XPATH,
            (
                f"//div[text()='{product_name}']"
                f"/ancestor::div[@class='inventory_item']//button"
            ),
        )
        self.driver.find_element(*locator).click()

    def go_to_cart(self) -> None:
        """
        Переходит на страницу корзины, кликнув по иконке корзины.
        """
        cart_icon = self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link"
        )
        cart_icon.click()
