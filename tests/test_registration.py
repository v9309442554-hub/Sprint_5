from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from locators import Locator
from generator import generate_login, generate_password


def test_registration():
    email = generate_login()
    password = generate_password()
    name = "Влад"

    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://stellarburgers.education-services.ru/register")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locator.NAME_FIELD)
    )

    # Заполняем форму регистрации
    driver.find_element(*Locator.NAME_FIELD).send_keys(name)
    driver.find_element(*Locator.EMAIL_FIELD).send_keys(email)
    driver.find_element(*Locator.PASSWORD_FIELD).send_keys(password)

    # Нажимаем кнопку регистрации
    driver.find_element(*Locator.SUBMIT_BUTTON).click()

    # Проверяем перенаправление на страницу логина
    WebDriverWait(driver, 10).until(
        EC.url_contains("/login")
    )
    assert driver.current_url == "https://stellarburgers.education-services.ru/login", \
        "Регистрация прошла успешно — перенаправление на /login"

    driver.quit()
