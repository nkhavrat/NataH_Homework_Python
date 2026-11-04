from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:

    DELAY_INPUT = (By.CSS_SELECTOR, '#delay')
    RESULT_VALUE = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver, url):
        """
        Конструктор класса CalculatorPage.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 50)

    @allure.step("Открытие страницы калькулятора")
    def open(self):
        """
        Открывает страницу калькулятора.
        """
        self.driver.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html"
            )

    @allure.step("Установка задержки {delay} секунд")
    def set_delay(self, delay):
        """
        Устанавливает задержку для выполнения операций на калькуляторе.

        :param delay: int — время задержки в секундах.
        """
        delay_input = self.wait.until(EC.presence_of_element_located(
            self.DELAY_INPUT
        ))
        delay_input.clear()
        delay_input.send_keys(delay)

    @allure.step("Нажатие кнопок: {buttons}")
    def enter_expression(self, buttons):
        """
        Нажимает на несколько кнопок калькулятора по очереди.
        :param buttons: list[str] — список текстов на кнопках,
        которые нужно нажать.
        """
        buttons = ["7", "+", "8", "="]
        for button in buttons:
            xpath = f"//span[text()='{button}']"
            self.driver.find_element(By.XPATH, xpath).click()

    @allure.step("На экране калькулятора результат '15'")
    def get_result(self):
        """
        Возвращает текущий результат с экрана калькулятора.

        :return: str — текст результата на экране калькулятора.
        """
        self.wait.until(EC.text_to_be_present_in_element(
            self.RESULT_VALUE, "15"))
        result_element = self.driver.find_element(*self.RESULT_VALUE)
        return result_element.text
