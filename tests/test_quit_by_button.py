from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from tests.locators import Locator

email = "v_88@yandex.ru"
password = "qwerty"

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=options)

# 1. Переходим на главную страницу
driver.get("https://stellarburgers.education-services.ru/")
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(Locator.ACCOUNT_BUTTON)
)

# 2. Нажимаем кнопку «Личный кабинет»
driver.find_element(*Locator.ACCOUNT_BUTTON).click()
WebDriverWait(driver, 10).until(
    EC.url_contains("/login")
)

# 3. Заполняем форму входа
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(Locator.LOGIN_EMAIL_FIELD)
)
driver.find_element(*Locator.LOGIN_EMAIL_FIELD).send_keys(email)
driver.find_element(*Locator.LOGIN_PASSWORD_FIELD).send_keys(password)

# 4. Нажимаем «Войти»
driver.find_element(*Locator.LOGIN_SUBMIT_BUTTON).click()

# 5. Проверяем, что попали в личный кабинет
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(Locator.LOGOUT_BUTTON)
)

# 6. Нажимаем кнопку «Личный кабинет» 
driver.find_element(*Locator.ACCOUNT_BUTTON).click()
WebDriverWait(driver, 10).until(
    EC.url_contains("/account")
)

# 7. Нажимаем кнопку «Выход»
driver.find_element(*Locator.LOGOUT_BUTTON).click()

# 8. Проверяем, что вышли — появилась кнопка «Личный кабинет»
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(Locator.ACCOUNT_BUTTON)
)
print("Выход из личного кабинета успешен, URL:", driver.current_url)

driver.quit()
