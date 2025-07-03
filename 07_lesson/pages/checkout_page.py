from selenium.webdriver.common.by import By
from time import sleep

class CheckoutPage:
    def __init__(self, driver): #Конструктор
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")

    #Def - метод
    def fill_form(self, first, last, zip_code):
        self.driver.find_element(*self.first_name).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.postal_code).send_keys(zip_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total(self):
        # Извлекаем текст из элемента Total
        total_element = self.driver.find_element(
            By.CLASS_NAME, "summary_total_label"
        )
        return total_element.text