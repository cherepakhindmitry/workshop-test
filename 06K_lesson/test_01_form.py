import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture
def driver():
    service = EdgeService(EdgeChromiumDriverManager().install())
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(service=service, options=options)
    yield driver
    driver.quit()


def test_form_validation(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )
    wait = WebDriverWait(driver, 10)

    # Ждём форму
    wait.until(EC.presence_of_element_located((By.NAME, "first-name")))

    # Заполняем поля, кроме zip-code
    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for name, value in fields.items():
        field = driver.find_element(By.NAME, name)
        field.send_keys(value)

    # Submit
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Проверка: zip-code должен быть с классом alert-danger (красный)
    zip_code_div = wait.until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )
    assert "alert-danger" in zip_code_div.get_attribute("class")

    # Остальные поля должны быть alert-success (зелёный)
    for name in fields.keys():
        el = wait.until(
            EC.presence_of_element_located((By.ID, name))
        )
        assert "alert-success" in el.get_attribute("class"), (
            f"{name} не подсвечен зелёным"
        )
