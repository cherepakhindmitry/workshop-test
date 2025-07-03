import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Создание и закрытие браузера
    driver = webdriver.Chrome()
    yield driver
    driver.quit()