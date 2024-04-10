from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import StellarburgersLocators
from data import StellarburgersTestsData
from conftest import driver

class TestSwitchPersonalAccount:
    def test_switch_to_personal_account(self, driver):
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

        WebDriverWait(driver, 10).until(
            expected_conditions.text_to_be_present_in_element(StellarburgersLocators.TITLE_PROFILE,
                                                              'Профиль'))
        title_profile = driver.find_element(*StellarburgersLocators.TITLE_PROFILE)

        assert title_profile.is_displayed()




