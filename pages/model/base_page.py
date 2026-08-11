from enum import Enum
from playwright.sync_api import Page, Locator
from pages.model.base_page_actions import BasePageActions
from pages.model.base_page_verifications import BasePageVerifications
from pages.model.base_page_helper import BasePageHelper


class LocatorStrategy(Enum):
    LOCATOR = "locator"
    ROLE_AND_DESCRIPTION = "role_and_description"
    TEXT = "text"

class BasePage:

    def __init__(self, page: Page):
        self.page = page
        self.actions = BasePageActions()
        self.verifications = BasePageVerifications()
        self.helper = BasePageHelper(page)

    def get_element(self, locator: str, strategy: LocatorStrategy, role=None, element_description="") -> Locator:
        element = None

        match(strategy):
            case LocatorStrategy.LOCATOR:
                element = self.get_element_by_locator(locator)
            case LocatorStrategy.ROLE_AND_DESCRIPTION:
                element = self.get_element_by_role_and_description(locator, role, element_description)
            case LocatorStrategy.TEXT:
                element = self.get_element_by_text(locator, element_description)
            case _:
                raise ValueError(f"Invalid 'strategy' value: {strategy}")
             
        if element.count() == 1:
            return element
        else:
            # if all else fails, try AI locator healing
            return self.helper.get_healed_element(element_description, locator)

    def get_element_by_locator(self, locator: str) -> Locator:
        return self.page.locator(locator)

    def get_element_by_role_and_description(self, locator: str, element_role, element_description: str) -> Locator:
        # try primary locator first
        element = self.get_element_by_locator(locator)
        if element.count() == 1:
            return element
        return element \
            .or_(self.page.get_by_role(element_role, name=element_description)) \
            .or_(self.page.get_by_text(element_description))

    def get_element_by_text(self, locator: str, element_description: str) -> Locator:
        element = self.get_element_by_locator(locator)
        if element.count() == 1:
            return element
        return element.or_(self.page.get_by_text(element_description))

    def get_element_from_list(self, locator: str, item_label) -> Locator:
        element = self.page.locator(locator).filter(has_text=item_label)
        if element.count() == 1:
            return element
        return self.helper.get_healed_elements(item_label, locator).filter(has_text=item_label)
        