from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Создаем драйвер для Google Chrome
driver = webdriver.Chrome()

try:
    # Переходим на страницу с динамическими ID
    driver.get("http://uitestingplayground.com/dynamicid")

    # Находим синюю кнопку по CSS-классу ".btn-primary"
    # Здесь не используем ID, т.к. оно динамическое
    button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")

    # Кликаем на кнопку
    button.click()

    # Ждем 1 секунду, чтобы увидеть эффект
    time.sleep(1)
finally:
    # Закрываем браузер
    driver.quit()
