import os
from dotenv import load_dotenv
from playwright.sync_api import expect

load_dotenv()

from .base_page import BasePage


class InventoryPage(BasePage):

    """
    Locator for Inventory page
    """

    INVENTORY_CONTAINER = ".inventory_container"
    INVENTORY_ITEMS = ".inventory_item"
    ITEM_NAME = ".inventory_item_name"
    ITEM_PRICE = ".inventory_item_price"
    ADD_TO_CART_BUTTON = 'button[id*="add-to-cart"]'
    REMOVE_BUTTON = 'button[id*="remove"]'
    SHOPPING_CART_BADGE = ".shopping_cart_badge"
    SHOPPING_CART_LINK = ".shopping_cart_link"
    BURGER_MENU = "#react-burger-menu-btn"
    LOGOUT_LINK = "#logout_sidebar_link"
    SORT_DROPDOWN = ".product_sort_container"

    def __init__(self, page):
        super().__init__(page)

    def verify_inventory_page_loaded(self):
        """Verify inventory page is loaded"""
        expect(self.page.locator(self.INVENTORY_CONTAINER)).to_be_visible()
        expect(self.page.locator(self.INVENTORY_ITEMS).first).to_be_visible()

    def get_inventory_items_count(self) -> int:
        """Get count of inventory items"""
        return self.page.locator(self.INVENTORY_ITEMS).count()

    def get_item_names(self) -> list:
        """Get all item names"""
        return self.page.locator(self.ITEM_NAME).all_text_contents()

    def get_item_prices(self) -> list:
        """Get all item prices"""
        return self.page.locator(self.ITEM_PRICE).all_text_contents()

    def add_item_to_cart_by_name(self, item_name: str):
        """Add specific item to cart by name"""
        item_locator = self.page.locator(self.INVENTORY_ITEMS).filter(
            has_text=item_name
        )
        add_button = item_locator.locator(self.ADD_TO_CART_BUTTON)
        add_button.click()

    def add_first_item_to_cart(self):
        """Add first item to cart"""
        self.page.locator(self.ADD_TO_CART_BUTTON).first.click()

    def get_cart_badge_count(self) -> str:
        """Get cart badge count"""
        if self.is_element_visible(self.SHOPPING_CART_BADGE):
            return self.get_text(self.SHOPPING_CART_BADGE)
        return "0"

    def click_cart(self):
        """Click shopping cart"""
        self.click_element(self.SHOPPING_CART_LINK)

    def sort_products(self, sort_option: str):
        """Sort products by given option"""
        self.page.select_option(self.SORT_DROPDOWN, sort_option)

    def logout(self):
        """Logout from application"""
        self.click_element(self.BURGER_MENU)
        self.click_element(self.LOGOUT_LINK)
