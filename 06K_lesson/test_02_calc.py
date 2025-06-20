import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    # Открываем страницу
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    wait = WebDriverWait(driver, 60)

    # Устанавливаем задержку на 45 секунд
    delay_input = wait.until(EC.presence_of_element_located((By.ID, "delay")))
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажимаем 7 + 8 =
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # Ожидаем появления результата
    wait.until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )

    # Проверяем результат
    screen_text = driver.find_element(By.CLASS_NAME, "screen").text
    assert screen_text == "15", f"Ожидалось 15, но получили {screen_text}"
