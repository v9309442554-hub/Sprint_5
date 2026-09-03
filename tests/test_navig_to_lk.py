from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from locators import Locator


def test_navigation_to_lk():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=options)

    # 1. Переходим на главную страницу
    driver.get("https://stellarburgers.education-services.ru/")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locator.ACCOUNT_BUTTON)
    )

    # 2. Нажимаем кнопку «Личный кабинет»
    driver.find_element(*Locator.ACCOUNT_BUTTON).click()

    # 3. Проверяем переход на страницу входа
    WebDriverWait(driver, 10).until(
        EC.url_contains("/login")
    )
    assert "/login" in driver.current_url, \
        f"Ожидался переход на /login, получено: {driver.current_url}"
    print("Переход по кнопке «Личный кабинет» успешен, URL:", driver.current_url)

    driver.quit()
