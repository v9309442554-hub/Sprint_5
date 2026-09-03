from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from tests.locators import Locator


def test_invalid_password_error():
    """Проверяет, что при некорректном пароле появляется сообщение об ошибке."""
    email = "v_88@yandex.ru"
    password = "qwert"
    name = "Влад"

    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=options)

    try:
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

        # Ждём и проверяем сообщение об ошибке "Некорректный пароль"
        error_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locator.ERROR_MESSAGE_INVALID_PASSWORD)
        )
        print("Отображено сообщение об ошибке:", error_element.text)
        assert error_element.text == "Некорректный пароль", \
            f"Ожидалось 'Некорректный пароль', получено: '{error_element.text}'"

    finally:
        driver.quit()


if __name__ == "__main__":
    test_invalid_password_error()
