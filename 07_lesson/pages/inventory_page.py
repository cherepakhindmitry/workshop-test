from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_name):
        # Преобразуем название в формат локатора
        locator = (
            By.XPATH, f"//div[text()='{product_name}']"
                      f"/ancestor::div[@class='inventory_item']//button"
        )
        self.driver.find_element(*locator).click()

    def go_to_cart(self):
        cart_icon = self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link"
        )
        cart_icon.click()
