from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Создаем Chrome-драйвер
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Переход на сайт с ленивой загрузкой изображений
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

    # Ждём, пока загрузится 3-я картинка (по CSS: img:nth-of-type(3))
    wait = WebDriverWait(driver, 10)
    third_img = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "img:nth-of-type(3)"))
    )

    # Получаем атрибут "src" (ссылка на изображение)
    print(third_img.get_attribute("src"))

finally:
    driver.quit()
