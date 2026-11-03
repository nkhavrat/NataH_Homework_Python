import pytest
from selenium import webdriver
from lesson_10.pages.calculator_page import CalculatorPage
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тестирование калькулятора: 7 + 8 = 15.")
@allure.description("Тест проверяет корректность"
                    " работы калькулятора ")
@allure.feature("Calculator")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator(driver):
    url = ("https://bonigarcia.dev/selenium-webdriver-java/"
           "slow-calculator.html")
    calc_page = CalculatorPage(driver, url)
    calc_page.open()
    calc_page.set_delay("45")
    calc_page.enter_expression(["7", "+", "8", "="])
    calc_page.get_result()
    with allure.step("Проверка результата"):
        assert calc_page.get_result() == "15"
