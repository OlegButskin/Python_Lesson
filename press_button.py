from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.ID, "ajaxButton").click()

element = driver.find_element(By.CSS_SELECTOR, "p.bg-success")

print(element.text)
