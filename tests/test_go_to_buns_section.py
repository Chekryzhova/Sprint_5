from locators import StellarburgersLocators
from conftest import driver

class TestGoToBunsSection:
    def test_go_to_buns_section(self, driver):
        sauces_section = driver.find_element(*StellarburgersLocators.SAUCES_SECTION)
        sauces_section.click()
        buns_section = driver.find_element(*StellarburgersLocators.BUNS_SECTION)
        buns_section.click()
        buns_title = driver.find_element(*StellarburgersLocators.TITLE_BUNS_LIST)
        assert buns_section.text == 'Булки' and buns_title.text == 'Булки'