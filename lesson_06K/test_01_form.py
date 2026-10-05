from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    wait = WebDriverWait(driver, 20)

    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro",
    }

    for name, value in fields.items():
        field = wait.until(EC.presence_of_element_located((By.NAME, name)))
        field.clear()
        field.send_keys(value)

    submit_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[type='submit']")))
    submit_button.click()

    wait.until(EC.presence_of_element_located((By.ID, "zip-code")))

    zip_code_field = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_code_field.get_attribute("class"), \
        "Поле Zip-code не подсвечено красным"

    fields_to_check = [
        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "company", "country", "job-position"
    ]

    for field_id in fields_to_check:
        field = driver.find_element(By.ID, field_id)
        assert "alert-success" in field.get_attribute("class"), \
            f"Поле {field_id} не подсвечено зеленым"

    driver.quit()
