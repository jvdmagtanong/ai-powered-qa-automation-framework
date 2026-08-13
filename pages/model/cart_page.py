from pages.model.base_page import BasePage, LocatorStrategy
from pages.locator.cart_locator import CartLocator

class CartPage(BasePage):

    def cart_inventory_item(self, item_label):
        return self.get_element_from_list(CartLocator.CART_INVENTORY_ITEM, item_label)

    def remove_button(self, item_label):
        role, name = CartLocator.REMOVE_BUTTON_ROLE
        return self.cart_inventory_item(item_label).get_by_role(role, name=name)

    def continue_shopping_button(self):
        role, name = CartLocator.CONTINUE_SHOPPING_BUTTON_ROLE
        return self.get_element(
            CartLocator.CONTINUE_SHOPPING_BUTTON, 
            LocatorStrategy.ROLE_AND_DESCRIPTION, 
            role=role, element_description=name
        )

    def checkout_button(self):
        role, name = CartLocator.CHECKOUT_BUTTON_ROLE
        return self.get_element(
            CartLocator.CHECKOUT_BUTTON, 
            LocatorStrategy.ROLE_AND_DESCRIPTION, 
            role=role, element_description=name
        )
    
    def verify_cart_inventory_item_visibility(self, item_label, isVisible=True):
        if isVisible:
            self.verifications.verify_element_is_visible(self.cart_inventory_item(item_label))
        else:
            self.verifications.verify_element_is_not_visible(self.cart_inventory_item(item_label))

