
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")


wait = WebDriverWait(driver, 10)
delay = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#delay")))

delay.clear()
delay.send_keys("45")


driver.find_element(By.XPATH, "//span[text()='7']").click()
driver.find_element(By.XPATH, "//span[text()='+']").click()
driver.find_element(By.XPATH, "//span[text()='8']").click()
driver.find_element(By.XPATH, "//span[text()='=']").click()


WebDriverWait(driver, 50).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), '15')
)


res = driver.find_element(By.CSS_SELECTOR, ".screen").text
assert res == '15', f"Ожидалось '15', но получено '{res}'"

driver.quit()
