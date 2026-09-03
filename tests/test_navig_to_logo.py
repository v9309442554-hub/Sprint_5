from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from locators import Locator


def test_navigation_to_logo():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=options)

    # 1. Переходим на главную страницу
    driver.get("https://stellarburgers.education-services.ru/")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locator.ACCOUNT_BUTTON)
    )

    # 2. Нажимаем кнопку «Личный кабинет» — переход на /login
    driver.find_element(*Locator.ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(
        EC.url_contains("/login")
    )

    # 3. Кликаем по логотипу
    driver.find_element(*Locator.LOGO_LINK).click()

    # 4. Проверяем переход на главную страницу
    WebDriverWait(driver, 10).until(
        EC.url_contains("/")
    )
    assert driver.current_url == "https://stellarburgers.education-services.ru/", \
        f"Ожидался переход на главную, получено: {driver.current_url}"
    print("Переход по логотипу из личного кабинета успешен, URL:", driver.current_url)

    driver.quit()
