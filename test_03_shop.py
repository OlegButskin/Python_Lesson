import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_fill_form(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение формы
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    # Нажатие кнопки
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Проверка подсветки поля Zip code
    zip_class = driver.find_element(By.ID, "zip-code").get_attribute("class")
    assert zip_class == "alert py-2 alert-danger", "Поле 'Zip code' не подсвечено как ошибка"

    # Проверка подсветки остальных полей
    fields = [
        "#first-name", "#last-name", "#address", "#city",
        "#country", "#e-mail", "#phone", "#company"
    ]
    for selector in fields:
        field_class = driver.find_element(By.CSS_SELECTOR, selector).get_attribute("class")
        assert field_class == "alert py-2 alert-success", f"{selector} не подсвечено как корректное"
