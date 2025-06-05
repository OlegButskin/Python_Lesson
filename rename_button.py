from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")

driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("Skypro")
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
print(driver.find_element(By.CSS_SELECTOR, "#updatingButton").text)
