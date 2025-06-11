from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Создаем драйвер для Firefox
driver = webdriver.Firefox()

try:
    # Открываем страницу с полем ввода
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Находим поле ввода по тегу input
    input_field = driver.find_element(By.TAG_NAME, "input")

    # Вводим текст "Sky"
    input_field.send_keys("Sky")
    time.sleep(1)  # Ждем 1 секунду

    # Очищаем поле ввода
    input_field.clear()
    time.sleep(1)  # Ждем 1 секунду

    # Вводим текст "Pro"
    input_field.send_keys("Pro")
    time.sleep(1)
finally:
    # Закрываем браузер
    driver.quit()
