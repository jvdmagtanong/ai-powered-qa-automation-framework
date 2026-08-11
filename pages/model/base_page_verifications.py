from playwright.sync_api import Locator, expect

class BasePageVerifications:
    
    def is_visible(self, locator: Locator):
        return locator.is_visible()

    def verify_element_has_text(self, locator: Locator, expected_text: str):
        expect(locator).to_have_text(expected_text)

    def verify_element_is_visible(self, locator: Locator):
        expect(locator).to_be_visible()

    def verify_element_is_not_visible(self, locator: Locator):
        expect(locator).not_to_be_visible()
