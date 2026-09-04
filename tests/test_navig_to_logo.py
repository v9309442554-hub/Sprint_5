from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locator
from fixtures import BASE_URL


class TestNavigationToLogo:
    def test_navigation_to_logo(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locator.ACCOUNT_BUTTON)
        )

        driver.find_element(*Locator.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_contains("/login"))

        driver.find_element(*Locator.LOGO_LINK).click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("/")
        )
        assert driver.current_url == BASE_URL
