# Импорт необходимых библиотек:
# webdriver — для управления браузером
# By — способ указать, как искать элемент (по ID, классу, тегу и т.д.)
# Service — для запуска ChromeDriver через webdriver-manager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time  # используется для паузы между действиями

# Создаем объект Chrome-драйвера, с автоматической установкой подходящего ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Открываем веб-страницу с кнопкой
    driver.get("http://uitestingplayground.com/classattr")

    # Находим кнопку по CSS-классу. В данном случае .btn-primary — синяя кнопка
    button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")

    # Кликаем по найденной кнопке
    button.click()

    # Делаем паузу, чтобы увидеть результат перед закрытием окна
    time.sleep(3)
finally:
    # Закрываем браузер даже если произошла ошибка
    driver.quit()
