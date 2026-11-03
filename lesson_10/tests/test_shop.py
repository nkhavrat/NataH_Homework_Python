import pytest
from selenium import webdriver
from lesson_10.pages.shop_page import MainShopPage
from lesson_10.pages.shop_page import CartPage
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тестирование интернет-магазина")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Добавление в корзину")
@allure.feature("Создание заказа")
def test_shop(driver):
    with allure.step("Авторизация"):
        shop_page = MainShopPage(driver, "https://www.saucedemo.com/")
    shop_page.open()
    shop_page.authorization()
    shop_page.get_add_product()
    shop_page.get_shopping_cart()
    with allure.step("Переход на страницу оформления заказа"):
        shop_page = CartPage(driver, "https://www.saucedemo.com/cart.html")
    shop_page.get_checkout()
    shop_page.get_form()
    shop_page.get_continue()
    shop_page.get_total()
    shop_page.get_result()
    with allure.step(f"Проверить значение итоговой суммы: {'Total: $58.29'}"):
        assert shop_page.get_result() == "Total: $58.29"
