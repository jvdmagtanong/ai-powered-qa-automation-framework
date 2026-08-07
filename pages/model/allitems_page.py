from pages.locator.allitems_locator import AllItemsLocator


class AllItemsPage:
    def __init__(self, page):
        self.page = page

    def add_or_remove_item_from_cart(self, item_label, isAdding: bool = True):
        item = self.page.locator(AllItemsLocator.INVENTORY_ITEM).filter(
            has_text=item_label
        )
        add_to_cart_role, add_to_cart_name = AllItemsLocator.ADD_TO_CART_BUTTON_ROLE
        remove_from_cart_role, remove_from_cart_name = AllItemsLocator.REMOVE_BUTTON_ROLE
        add_to_cart_button = item.get_by_role(add_to_cart_role, name=add_to_cart_name)
        remove_button = item.get_by_role(remove_from_cart_role, name=remove_from_cart_name)

        if isAdding:
            if add_to_cart_button.is_visible():
                add_to_cart_button.click()
        else:
            if remove_button.is_visible():
                remove_button.click()


