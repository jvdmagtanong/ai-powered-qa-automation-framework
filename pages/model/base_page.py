from playwright.sync_api import Page, Locator, expect
import allure


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def click(self, locator: Locator):
        locator.click()

    def fill(self, locator: Locator, text: str):
        locator.fill(text)

    def get_text(self, locator: Locator):
        return locator.text_content()

    def is_visible(self, locator: Locator):
        return locator.is_visible()

    def wait_for_visible(self, locator: Locator):
        locator.wait_for(state="visible")

    def verify_element_has_text(self, locator: Locator, expected_text: str):
        expect(locator).to_have_text(expected_text)

    def verify_element_is_visible(self, locator: Locator):
        expect(locator).to_be_visible()

    def verify_element_is_not_visible(self, locator: Locator):
        expect(locator).not_to_be_visible()

    def take_screenshot(self, name: str):
        screenshot = f"test-reports/screenshots/{name}.png"

        self.page.screenshot(path=screenshot)

        allure.attach.file(
            screenshot,
            name=name,
            attachment_type=allure.attachment_type.PNG
        )