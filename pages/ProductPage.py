from selenium.webdriver.common.by import By

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_id):
        product_locator = (By.ID, f"add-to-cart-{product_id}")
        self.driver.find_element(*product_locator).click()

    def go_to_cart(self):
        cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        self.driver.find_element(*cart_icon).click()
