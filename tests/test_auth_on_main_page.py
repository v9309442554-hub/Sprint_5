from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



driver = webdriver.Chrome()

driver.get("https://stellarburgers.education-services.ru/register")
WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='text' and @name='name']")))

email = "v_88@yandex.ru"
password = "qwerty"


driver.find_element(
        By.XPATH,
        "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_size_large__G21Vg') and text()='Войти в аккаунт']",
    ).click()

driver.find_element(
        By.XPATH,
        "//div[contains(@class, 'input_type_text') and contains(@class, 'input_size_default')]//input[@type='text' and @name='name']",
    ).send_keys(email)

driver.find_element(
        By.XPATH,
        "//div[contains(@class, 'input_type_password') and contains(@class, 'input_size_default')]//input[@type='password' and @name='Пароль']",
    ).send_keys(password)

driver.find_element (
        By.XPATH,
        "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_type_primary__1O7Bx') and text()='Войти']",
    ).click()


driver.quit()