import pytest
from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.ProductPage import ProductsPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_add_to_cart_and_checkout(driver):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products_page.add_to_cart("sauce-labs-backpack")
    products_page.add_to_cart("sauce-labs-bolt-t-shirt")
    products_page.add_to_cart("sauce-labs-onesie")
    products_page.go_to_cart()

    cart_page.proceed_to_checkout()

    checkout_page.fill_checkout_info("John", "Doe", "12345")
    total = checkout_page.get_total_price()

    assert total == "58.29", f"Ожидалось '58.29', но получено '{total}'"
