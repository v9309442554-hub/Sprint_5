from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from tests.locators import Locator

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=options)

# 1. Переходим на главную страницу
driver.get("https://stellarburgers.education-services.ru/")
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(Locator.CONSTRUCTOR_SECTION)
)

# 2. Нажимаем вкладку «Соусы»
driver.find_element(*Locator.SAUCE_TAB).click()

# 3. Проверяем, что отображается раздел соусов
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(Locator.SPICY_X_SAUCE)
)
print("Переход к разделу «Соусы» успешен, URL:", driver.current_url)

driver.quit()
