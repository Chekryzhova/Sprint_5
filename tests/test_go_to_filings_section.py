from locators import StellarburgersLocators
from conftest import driver

class TestGoToFilingsSection:
    def test_go_to_filings_section(self, driver):
        filings_section = driver.find_element(*StellarburgersLocators.FILINGS_SECTION)
        filings_section.click()
        filings_title = driver.find_element(*StellarburgersLocators.TITLE_FILINGS_LIST)
        assert filings_section.text == 'Начинки' and filings_title.text == 'Начинки'