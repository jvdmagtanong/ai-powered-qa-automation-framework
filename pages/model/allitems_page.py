from pages.model.base_page import BasePage
from pages.locator.allitems_locator import AllItemsLocator


class AllItemsPage(BasePage):

    def add_or_remove_item_from_cart(self, item_label, isAdding: bool = True):
        item = self.get_element_from_list(AllItemsLocator.INVENTORY_ITEM, item_label)
        role, name = None, None
        button = None

        if isAdding:
            role, name = AllItemsLocator.ADD_TO_CART_BUTTON_ROLE
        else:
            role, name = AllItemsLocator.REMOVE_BUTTON_ROLE

        button = item.get_by_role(role, name=name)
        self.actions.click(button)
