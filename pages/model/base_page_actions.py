from playwright.sync_api import Locator

class BasePageActions:

    def click(self, locator: Locator):
        locator.click()

    def fill(self, locator: Locator, text: str):
        locator.fill(text)

    def get_text(self, locator: Locator):
        return locator.text_content()
    
    def wait_for_visible(self, locator: Locator):
        locator.wait_for(state="visible")