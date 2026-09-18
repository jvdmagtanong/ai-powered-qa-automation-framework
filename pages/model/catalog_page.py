from distro import name

from pages.model.base_page import BasePage
from pages.locator.catalog_locator import CatalogLocator


class CatalogPage(BasePage):

    def add_or_remove_item_from_cart(self, item_label, isAdding: bool = True):
        item = self.get_element_from_list(CatalogLocator.INVENTORY_ITEM, item_label)
        role, name = None, None
        button = None

        if isAdding:
            role, name = CatalogLocator.ADD_TO_CART_BUTTON_ROLE
        else:
            role, name = CatalogLocator.REMOVE_BUTTON_ROLE

        button = item.get_by_role(role, name=name)
        self.actions.click(button)

    def verify_add_to_cart_button_is_displayed(self, item_label):
        item = self.get_element_from_list(CatalogLocator.INVENTORY_ITEM, item_label)
        role, name = CatalogLocator.ADD_TO_CART_BUTTON_ROLE
        button = item.get_by_role(role, name=name)
        self.verifications.verify_element_is_visible(button)

    def verify_remove_button_is_displayed(self, item_label):
        item = self.get_element_from_list(CatalogLocator.INVENTORY_ITEM, item_label)
        role, name = CatalogLocator.REMOVE_BUTTON_ROLE
        button = item.get_by_role(role, name=name)
        self.verifications.verify_element_is_visible(button)
 