from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locator
from conftest import BASE_URL
from data.test_data import AUTH_EMAIL, AUTH_PASSWORD


class TestAuthByFormRegistration:
    def test_auth_by_form_registration(self, driver):
        driver.get(f"{BASE_URL}register")
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locator.NAME_FIELD)
        )

        driver.find_element(*Locator.LOGIN_FROM_REGISTER_LINK).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locator.LOGIN_EMAIL_FIELD)
        )
        driver.find_element(*Locator.LOGIN_EMAIL_FIELD).send_keys(AUTH_EMAIL)
        driver.find_element(*Locator.LOGIN_PASSWORD_FIELD).send_keys(AUTH_PASSWORD)

        driver.find_element(*Locator.LOGIN_SUBMIT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locator.ORDER_BUTTON)
        )
        assert driver.find_element(*Locator.ORDER_BUTTON).is_displayed()
