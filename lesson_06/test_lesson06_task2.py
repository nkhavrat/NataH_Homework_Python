from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 5)

    driver.get("https://gitflic.ru/")
    driver.maximize_window()

    driver.add_cookie({
        "name": "SESSION",
        "value":
            "OGUzNTUxMzAtMDFlNC00NWU5LThjNzQtMTcwMmRmYmIyNWNm",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })

    driver.refresh()
    driver.get("https://gitflic.ru/user/khavrat")

    url_user1 = driver.current_url
    driver.delete_all_cookies()
    driver.refresh()

    driver.add_cookie({
        "name": "SESSION",
        "value": "YWU5NWQ0ZjEtZjJiZi00YjMxLThmOTMtMjljYmZhNWU3NDBl",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })

    driver.refresh()
    driver.get("https://gitflic.ru/user/obrosov")
    url_user2 = driver.current_url

    assert url_user1 != url_user2

    driver.quit()
