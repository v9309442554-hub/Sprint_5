from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from locators import Locator
from conftest import BASE_URL
from data.test_data import AUTH_EMAIL, AUTH_PASSWORD


class TestAuthOnMainPage:
    def test_auth_on_main_page(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locator.LOGIN_ACCOUNT_BUTTON)
        )

        driver.find_element(*Locator.LOGIN_ACCOUNT_BUTTON).click()

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

        driver.find_element(*Locator.ORDER_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button'))
        )
