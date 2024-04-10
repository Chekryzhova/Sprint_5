from locators import StellarburgersLocators
from conftest import driver

class TestGoToSaucesSection:
    def test_go_to_sauces_section(self, driver):
        sauces_section = driver.find_element(*StellarburgersLocators.SAUCES_SECTION)
        sauces_section.click()
        sauces_title = driver.find_element(*StellarburgersLocators.TITLE_SAUCES_LIST)
        assert sauces_section.text == 'Соусы' and sauces_title.text == 'Соусы'

