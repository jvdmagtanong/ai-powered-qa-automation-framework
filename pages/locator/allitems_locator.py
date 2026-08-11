from playwright.sync_api import Page

class AllItemsLocator:

    INVENTORY_ITEM = "[data-test='inventory-item']"
    ADD_TO_CART_BUTTON_ROLE = ("button", "Add to cart")
    REMOVE_BUTTON_ROLE = ("button", "Remove")
    BACKPACK_ADD_TO_CART_BUTTON = "[data-test='add-to-cart-sauce-labs-backpack']"
    BACKPACK_REMOVE_FROM_CART_BUTTON = "[data-test='remove-sauce-labs-backpack']"

    