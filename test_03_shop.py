from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка драйвера
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

# Открываем сайт
driver.get("https://www.saucedemo.com/")

# Авторизация как standard_user
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Добавление товаров в корзину
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

# Переход в корзину
cart_element = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_link"))
)
cart_element.click()

# Переход к оформлению заказа
driver.find_element(By.ID, "checkout").click()

# Заполнение формы
driver.find_element(By.ID, "first-name").send_keys("Ivan")
driver.find_element(By.ID, "last-name").send_keys("Petrov")
driver.find_element(By.ID, "postal-code").send_keys("123456")
driver.find_element(By.ID, "continue").click()

# Чтение итоговой стоимости
total_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
)
total_text = total_element.text

# Проверка стоимости
assert total_text == "Total: $58.29", f"Ожидалось 'Total: $58.29', но получено '{total_text}'"

# Закрытие браузера
#driver.quit()
