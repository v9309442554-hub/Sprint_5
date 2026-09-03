from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from tests.locators import Locator


def test_auth_by_lk_button():
    email = "v_88@yandex.ru"
    password = "qwerty"

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

    # 3. Заполняем форму входа
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locator.LOGIN_EMAIL_FIELD)
    )
    driver.find_element(*Locator.LOGIN_EMAIL_FIELD).send_keys(email)
    driver.find_element(*Locator.LOGIN_PASSWORD_FIELD).send_keys(password)

    # 4. Нажимаем «Войти»
    driver.find_element(*Locator.LOGIN_SUBMIT_BUTTON).click()

    # 5. Проверяем авторизацию — появление кнопки «Выход»
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locator.LOGOUT_BUTTON)
    )
    assert driver.find_element(*Locator.LOGOUT_BUTTON).is_displayed(), \
        "Кнопка «Выход» не отображается — авторизация не прошла"
    print("Аутентификация успешна, URL:", driver.current_url)


    driver.quit()

