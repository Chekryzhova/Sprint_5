from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import StellarburgersLocators
from data import StellarburgersTestsData
from conftest import driver
class TestLogoutFromPersonalAccount:
    def test_logout_from_personal_account(self, driver):
        login_to_account = driver.find_element(*StellarburgersLocators.LOGIN_TO_ACCOUNT_BUTTON)
        login_to_account.click()
        login_email_input = driver.find_element(*StellarburgersLocators.LOGIN_EMAIL_INPUT)
        login_email_input.send_keys(StellarburgersTestsData.LOGIN_EMAIL)
        login_password_input = driver.find_element(*StellarburgersLocators.LOGIN_PASSWORD_INPUT)
        login_password_input.send_keys(StellarburgersTestsData.REGISTRATION_PASSWORD)
        login_button = driver.find_element(*StellarburgersLocators.LOGIN_BUTTON)
        login_button.click()
        personal_account_button = driver.find_element(*StellarburgersLocators.PERSONAL_ACCOUNT_BUTTON)
        personal_account_button.click()
        logout_button = driver.find_element(*StellarburgersLocators.LOGOUT_BUTTON)
        logout_button.click()

        WebDriverWait(driver, 10).until(
            expected_conditions.text_to_be_present_in_element(StellarburgersLocators.ENTRANCE, 'Вход'))
        entrance = driver.find_element(*StellarburgersLocators.ENTRANCE)

        assert entrance.is_displayed()

