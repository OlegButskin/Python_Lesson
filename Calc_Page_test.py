from selenium import webdriver
from pages.PageCalculator import CalculatorPage

def test_calculator():
    driver = webdriver.Chrome()
    calculator = CalculatorPage(driver)
    calculator.open()
    calculator.set_delay(45)

    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    calculator.click_button("=")

    calculator.wait_for_result("15", timeout=50)

    result = calculator.get_result()
    assert result == "15"

    driver.quit()
