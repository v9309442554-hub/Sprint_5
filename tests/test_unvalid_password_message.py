from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locator
from fixtures import BASE_URL
from data.test_data import REGISTRATION_NAME, AUTH_EMAIL, INVALID_PASSWORD


class TestInvalidPasswordMessage:
    def test_invalid_password_error(self, driver):
        driver.get(f"{BASE_URL}register")
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locator.NAME_FIELD)
        )

        driver.find_element(*Locator.NAME_FIELD).send_keys(REGISTRATION_NAME)
        driver.find_element(*Locator.EMAIL_FIELD).send_keys(AUTH_EMAIL)
        driver.find_element(*Locator.PASSWORD_FIELD).send_keys(INVALID_PASSWORD)

        driver.find_element(*Locator.SUBMIT_BUTTON).click()

        error_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locator.ERROR_MESSAGE_INVALID_PASSWORD)
        )
        assert error_element.text == "Некорректный пароль"
