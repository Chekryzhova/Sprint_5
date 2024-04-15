from data import StellarburgersTestsData
from locators import StellarburgersLocators
from conftest import driver

class TestInvalidPasswordRegistration:
    def test_invalid_password(self, driver):
        login_to_account = driver.find_element(*StellarburgersLocators.LOGIN_TO_ACCOUNT_BUTTON)
        login_to_account.click()
        register_button = driver.find_element(*StellarburgersLocators.REGISTER_BUTTON)
        register_button.click()
        name_input = driver.find_element(*StellarburgersLocators.NAME_INPUT)
        name_input.send_keys(StellarburgersTestsData.REGISTRATION_NAME)
        email_input = driver.find_element(*StellarburgersLocators.EMAIL_INPUT)
        email_input.send_keys(StellarburgersTestsData.REGISTRATION_MAIL)
        password_input = driver.find_element(*StellarburgersLocators.PASSWORD_INPUT)
        password_input.send_keys('12')
        registration_button = driver.find_element(*StellarburgersLocators.REGISTRATION_BUTTON)
        registration_button.click()
        invalid_password = driver.find_element(*StellarburgersLocators.INVALID_PASSWORD)

        assert invalid_password.is_displayed()