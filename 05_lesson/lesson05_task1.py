from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Создаем объект драйвера для Google Chrome
driver = webdriver.Chrome()

try:
    # Открываем страницу
    driver.get("http://uitestingplayground.com/classattr")

    # Находим кнопку по CSS-классу ".btn-primary"
    button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")

    # Кликаем на найденную кнопку
    button.click()

    # Ждем 1 секунду, чтобы увидеть результат клика
    time.sleep(1)
finally:
    # Закрываем браузер вне зависимости от результата
    driver.quit()
