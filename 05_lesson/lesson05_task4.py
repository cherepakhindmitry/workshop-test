from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Создаем драйвер для Firefox
driver = webdriver.Firefox()

try:
    # Открываем страницу авторизации
    driver.get("http://the-internet.herokuapp.com/login")

    # Вводим username
    driver.find_element(By.ID, "username").send_keys("tomsmith")

    # Вводим password
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    # Нажимаем кнопку Login
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    time.sleep(1)  # Ждем загрузки

    # Получаем текст с зеленой плашки (успешный вход)
    message = driver.find_element(By.CSS_SELECTOR, "div.flash.success").text

    # Выводим сообщение в консоль
    print(message.strip())
finally:
    # Закрываем браузер
    driver.quit()
