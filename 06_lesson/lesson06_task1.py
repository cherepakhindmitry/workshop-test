from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
# Запуск Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Загружаем страницу
    driver.get("http://uitestingplayground.com/ajax")

    # Явно ждём появления кнопки с ID 'ajaxButton'
    wait = WebDriverWait(driver, 20)
    button = wait.until(EC.element_to_be_clickable((By.ID, "ajaxButton")))

    # Кликаем
    button.click()

    # Ждём, пока появится зелёная плашка
    message = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
    )

    # Выводим текст
    print(message.text)

finally:
    driver.quit()
