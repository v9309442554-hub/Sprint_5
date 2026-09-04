from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from locators import Locator
from conftest import BASE_URL


class TestNavigSections:
    def test_navig_sauces(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locator.CONSTRUCTOR_SECTION)
        )

        driver.find_element(*Locator.SAUCE_TAB).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locator.SPICY_X_SAUCE)
        )
        assert driver.find_element(*Locator.SAUCE_TAB).is_displayed()

    def test_navig_fillings(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locator.CONSTRUCTOR_SECTION)
        )

        driver.find_element(*Locator.FILLINGS_TAB).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locator.PROTOSTOMIA_MEAT)
        )
        assert driver.find_element(*Locator.FILLINGS_TAB).is_displayed()

    def test_navig_sauces_to_buns(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locator.CONSTRUCTOR_SECTION)
        )

        driver.find_element(*Locator.SAUCE_TAB).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locator.SPICY_X_SAUCE)
        )
        assert driver.find_element(*Locator.SAUCE_TAB).is_displayed()

        driver.find_element(*Locator.BUNS_TAB).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locator.R2D3_BUN)
        )
        assert driver.find_element(*Locator.BUNS_TAB).is_displayed()
