from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("http://uitestingplayground.com/classattr")
    button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()
    time.sleep(5)
finally:
    driver.quit()
