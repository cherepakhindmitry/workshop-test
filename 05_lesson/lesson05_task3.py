from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

# Запускаем браузер Firefox через менеджер драйверов GeckoDriver
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

try:
    # Открываем сайт с полем ввода
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Находим элемент ввода по тегу <input>
    input_field = driver.find_element(By.TAG_NAME, "input")

    # Вводим текст "Sky"
    input_field.send_keys("Sky")
    time.sleep(1)

    # Очищаем поле ввода методом clear()
    input_field.clear()
    time.sleep(1)

    # Вводим новый текст "Pro"
    input_field.send_keys("Pro")
    time.sleep(2)
finally:
    # Закрываем браузер
    driver.quit()
