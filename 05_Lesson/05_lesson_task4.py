from pyexpat.errors import messages
from selenium import webdriver

from selenium.webdriver.common.by import By


driver = webdriver.Firefox()


driver.get("http://the-internet.herokuapp.com/login")

username_locator = "#username"
password_locator = "#password"
login_button = '[class*="sign-in"]'
success_message_locator = "#flash"

username_field = driver.find_element(By.CSS_SELECTOR, username_locator)
username_field.send_keys("tomsmith")

password_field = driver.find_element(By.CSS_SELECTOR, password_locator)
password_field.send_keys("SuperSecretPassword!")

login_button = driver.find_element(By.CSS_SELECTOR, login_button)
login_button.click()

success_message = driver.find_element(By.CSS_SELECTOR, success_message_locator)
print(success_message.text.strip())   # -> "You logged into a secure area!"

driver.quit()




