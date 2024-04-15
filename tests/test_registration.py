from data import StellarburgersTestsData
from locators import StellarburgersLocators
from conftest import driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestStellarburgersRegistration:
    def test_registration(self, driver):
        login_to_account = driver.find_element(*StellarburgersLocators.LOGIN_TO_ACCOUNT_BUTTON)
        login_to_account.click()
        register_button = driver.find_element(*StellarburgersLocators.REGISTER_BUTTON)
        register_button.click()
        name_input = driver.find_element(*StellarburgersLocators.NAME_INPUT)
        name_input.send_keys(StellarburgersTestsData.REGISTRATION_NAME)
        email_input = driver.find_element(*StellarburgersLocators.EMAIL_INPUT)
        email_input.send_keys(StellarburgersTestsData.REGISTRATION_MAIL)
        password_input = driver.find_element(*StellarburgersLocators.PASSWORD_INPUT)
        password_input.send_keys(StellarburgersTestsData.REGISTRATION_PASSWORD)
        registration_button = driver.find_element(*StellarburgersLocators.REGISTRATION_BUTTON)
        registration_button.click()

        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element(StellarburgersLocators.ENTRANCE, 'Вход'))
        entrance = driver.find_element(*StellarburgersLocators.ENTRANCE)

        assert entrance.is_displayed()


