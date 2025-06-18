from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Запускаем Chrome с автоматическим драйвером
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Переход на нужную страницу
    driver.get("http://uitestingplayground.com/textinput")

    # Находим поле ввода и вводим текст "SkyPro"
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("SkyPro")

    # Находим кнопку и нажимаем
    driver.find_element(By.ID, "updatingButton").click()

    # Ждём, пока у кнопки изменится текст
    wait = WebDriverWait(driver, 5)
    updated_button = wait.until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
    )

    # Повторно находим кнопку (уже обновлённую) и выводим её текст
    button = driver.find_element(By.ID, "updatingButton")
    print(button.text)  # Ожидается: "SkyPro"

finally:
    driver.quit()
