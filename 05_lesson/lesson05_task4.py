from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

# Запускаем Firefox с автоподключением драйвера
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

try:
    # Открываем страницу авторизации
    driver.get("http://the-internet.herokuapp.com/login")

    # Вводим логин в поле username (находим по ID)
    driver.find_element(By.ID, "username").send_keys("tomsmith")

    # Вводим пароль в поле password
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    # Нажимаем кнопку входа (по тегу <button>)
    driver.find_element(By.TAG_NAME, "button").click()

    # Получаем текст из зеленой плашки (элемент с ID flash)
    message = driver.find_element(By.ID, "flash").text

    # Выводим сообщение в консоль
    print(message)

    time.sleep(2)
finally:
    # Закрываем браузер
    driver.quit()
