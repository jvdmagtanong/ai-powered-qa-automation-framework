from pages.model.base_page import BasePage
from pages.locator.cart_locator import CartLocator

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def cart_inventory_item(self, item_label):
        return self.page.locator(CartLocator.CART_INVENTORY_ITEM).filter(
            has_text=item_label
        )

    def remove_button(self, item_label):
        role, name = CartLocator.REMOVE_BUTTON_ROLE
        return self.cart_inventory_item(item_label).get_by_role(role, name=name)

    def continue_shopping_button(self):
        role, name = CartLocator.CONTINUE_SHOPPING_BUTTON_ROLE
        return self.page.locator(CartLocator.CONTINUE_SHOPPING_BUTTON).or_(
            self.page.get_by_role(role, name=name)
        )

    def checkout_button(self):
        role, name = CartLocator.CHECKOUT_BUTTON_ROLE
        return self.page.locator(CartLocator.CHECKOUT_BUTTON).or_(
            self.page.get_by_role(role, name=name)
        )

    def expect_cart_inventory_item_toBeVisible(self, item_label, isVisible=True):
        if isVisible:
            self.verify_element_is_visible(self.cart_inventory_item(item_label))
        else:
            self.verify_element_is_not_visible(self.cart_inventory_item(item_label))