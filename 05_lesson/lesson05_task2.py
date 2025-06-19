from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Открываем страницу с кнопкой, у которой динамический ID
    driver.get("http://uitestingplayground.com/dynamicid")

    # Ищем кнопку по CSS-классу. Он остается постоянным, даже если ID меняется
    button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")

    # Кликаем по кнопке
    button.click()
    time.sleep(3)
finally:
    # Закрываем браузер
    driver.quit()
