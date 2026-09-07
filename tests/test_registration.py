from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locator
from conftest import BASE_URL
from generator import generate_login, generate_password
from data.test_data import REGISTRATION_NAME


class TestRegistration:
    def test_registration(self, driver):
        email = generate_login()
        password = generate_password()

        driver.get(f"{BASE_URL}register")
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locator.NAME_FIELD)
        )

        driver.find_element(*Locator.NAME_FIELD).send_keys(REGISTRATION_NAME)
        driver.find_element(*Locator.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locator.PASSWORD_FIELD).send_keys(password)

        driver.find_element(*Locator.SUBMIT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        assert driver.current_url == f"{BASE_URL}login"
