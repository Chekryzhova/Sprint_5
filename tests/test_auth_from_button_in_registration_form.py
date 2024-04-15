from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import StellarburgersLocators
from data import StellarburgersTestsData
from conftest import driver

class TestAuthFromButtonInRegistrationForm:
    def test_auth_from_button_in_registration_form(self, driver):
        login_to_account = driver.find_element(*StellarburgersLocators.LOGIN_TO_ACCOUNT_BUTTON)
        login_to_account.click()
        register_button = driver.find_element(*StellarburgersLocators.REGISTER_BUTTON)
        register_button.click()
        login_button_in_registration_form = driver.find_element(*StellarburgersLocators.LOGIN_BUTTON_IN_REGISTRATION_OR_RECOVERY_FORM)
        login_button_in_registration_form.click()
        login_email_input = driver.find_element(*StellarburgersLocators.LOGIN_EMAIL_INPUT)
        login_email_input.send_keys(StellarburgersTestsData.LOGIN_EMAIL)
        login_password_input = driver.find_element(*StellarburgersLocators.LOGIN_PASSWORD_INPUT)
        login_password_input.send_keys(StellarburgersTestsData.REGISTRATION_PASSWORD)
        login_button = driver.find_element(*StellarburgersLocators.LOGIN_BUTTON)
        login_button.click()

        WebDriverWait(driver, 10).until(
            expected_conditions.text_to_be_present_in_element(StellarburgersLocators.PLACE_ORDER_BUTTON,
                                                              'Оформить заказ'))
        place_order_button = driver.find_element(*StellarburgersLocators.PLACE_ORDER_BUTTON)

        assert place_order_button.is_displayed()


