from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locator
from fixtures import BASE_URL


class TestNavigationToConstructor:
    def test_navigation_to_constructor(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locator.ACCOUNT_BUTTON)
        )

        driver.find_element(*Locator.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_contains("/login"))

        driver.find_element(*Locator.CONSTRUCTOR_LINK).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locator.CONSTRUCTOR_SECTION)
        )
