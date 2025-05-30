import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")


    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    yield driver
    driver.quit()

def test_add_to_cart_and_checkout(driver):
    #Добавление товаров
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    #Переход в корзину
    cart_element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'shopping_cart_link')))
    cart_element.click()

    # Checkout
    driver.find_element(By.ID, 'checkout').click()

    #Заполнение формы
    driver.find_element(By.ID, 'first-name').send_keys('John')
    driver.find_element(By.ID, 'last-name').send_keys('Doe')
    driver.find_element(By.ID, 'postal-code').send_keys("12345")
    driver.find_element(By.ID, 'continue').click()


    total_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
    text = total_element.text
    assert text == "Total: $58.29", f"Ожидалось 'Total: $58.29', но получено '{text}'"
