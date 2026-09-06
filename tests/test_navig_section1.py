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
            EC.presence_of_element_located(Locator.ACTIVE_TAB)
        )
        assert driver.find_element(*Locator.SAUCE_TAB).get_attribute("class") == \
            driver.find_element(*Locator.ACTIVE_TAB).get_attribute("class")

    def test_navig_fillings(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locator.CONSTRUCTOR_SECTION)
        )

        driver.find_element(*Locator.FILLINGS_TAB).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locator.ACTIVE_TAB)
        )
        assert driver.find_element(*Locator.FILLINGS_TAB).get_attribute("class") == \
            driver.find_element(*Locator.ACTIVE_TAB).get_attribute("class")

    def test_navig_sauces_to_buns(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locator.CONSTRUCTOR_SECTION)
        )

        driver.find_element(*Locator.SAUCE_TAB).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locator.ACTIVE_TAB)
        )
        assert driver.find_element(*Locator.SAUCE_TAB).get_attribute("class") == \
            driver.find_element(*Locator.ACTIVE_TAB).get_attribute("class")

        driver.find_element(*Locator.BUNS_TAB).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locator.ACTIVE_TAB)
        )
        assert driver.find_element(*Locator.BUNS_TAB).get_attribute("class") == \
            driver.find_element(*Locator.ACTIVE_TAB).get_attribute("class")
