import allure
from utils.dom_sanitizer import sanitize_dom
from utils.gemini_locator_healer import suggest_locator_for_element, suggest_locator_for_elements
from playwright.sync_api import Locator, Page


class BasePageHelper:
    
    def __init__(self, page: Page):
        self.page = page

    def get_healed_element(self, element_description: str, failed_locator: str) -> Locator:
        return self._heal_locator(
                element_description=element_description,
                failed_locator=failed_locator,
                suggest_function=suggest_locator_for_element,
                validation=lambda locator: locator.count() == 1
            )

    def get_healed_elements(self, element_description: str, failed_locator: str) -> Locator:
        return self._heal_locator(
                element_description=element_description,
                failed_locator=failed_locator,
                suggest_function=suggest_locator_for_elements,
                validation=lambda locator: locator.count() > 0
            )

    def _heal_locator(self, element_description: str, failed_locator: str, suggest_function, validation) -> Locator:
        with allure.step("AI Locator Healing - Standard locator failed"):
            self._attach_failed_locator(failed_locator)

            page_source = sanitize_dom(self.page.content())

            suggested_locator = suggest_function(
                element_description=element_description,
                failed_locator=failed_locator,
                page_source=page_source
            )

            if not suggested_locator:
                self._attach_healing_result("FAILED - Gemini did not provide a locator")
                return self.page.locator(failed_locator)

            healed_locator = self.page.locator(suggested_locator)

            if not validation(healed_locator):
                self._attach_healing_result("FAILED - AI suggested locator could not be validated")
                return self.page.locator(failed_locator)

            self._attach_suggested_locator(suggested_locator)
            self._attach_healing_result("SUCCESS - Locator validated and used")

            return healed_locator

    def _attach_failed_locator(self, locator: str):
        allure.attach(
            locator,
            name="Failed Locator",
            attachment_type=allure.attachment_type.TEXT
        )

    def _attach_suggested_locator(self, locator: str):
        allure.attach(
            locator,
            name="AI Suggested Locator",
            attachment_type=allure.attachment_type.TEXT
        )


    def _attach_healing_result(self, result: str):
        allure.attach(
            result,
            name="AI Healing Result",
            attachment_type=allure.attachment_type.TEXT
        )

