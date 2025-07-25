from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """Класс для взаимодействия со страницей логина сайта saucedemo.com."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация драйвера и локаторов.

        :param driver: Экземпляр WebDriver.
        """
        self.driver = driver
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self) -> None:
        """
        Открывает страницу авторизации saucedemo.
        """
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход в систему.

        :param username: Имя пользователя.
        :param password: Пароль.
        """
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_button).click()
