from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_images_loaded():
    # Создаем Chrome-драйвер
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 15)

    try:
        # Открываем страницу
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
        )

        # Ждем появления текста "Done!"
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "p"), "Done!"))

        # Получаем третье изображение
        third_img = driver.find_element(By.CSS_SELECTOR, "img:nth-of-type(3)")
        src = third_img.get_attribute("src")
        print(f"Третье изображение загружено: {src}")

        # Проверка
        assert "img" in src, f"Ожидалась ссылка на изображение, но получили: {src}"

    finally:
        driver.quit()
