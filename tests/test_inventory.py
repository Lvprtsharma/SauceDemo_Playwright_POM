import pytest
from utils.test_data import TestData


@pytest.mark.regression
class TestInventory:
    """Inventory page functionality tests"""

    def test_inventory_page_loads_correctly(self, authenticated_user, inventory_page):
        """Test that inventory page loads with all products"""
        inventory_page.verify_inventory_page_loaded()

        items_count = inventory_page.get_inventory_items_count()
        assert items_count == 6, f"Expected 6 items, but found {items_count}"

        item_names = inventory_page.get_item_names()
        for product in TestData.PRODUCTS:
            assert product in item_names, f"Product {product} not found in inventory"

    def test_add_single_item_to_cart(self, authenticated_user, inventory_page):
        """Test adding a single item to cart"""
        inventory_page.add_item_to_cart_by_name("Sauce Labs Backpack")

        cart_count = inventory_page.get_cart_badge_count()
        assert cart_count == "1", f"Expected cart count to be 1, but got {cart_count}"

    def test_add_multiple_items_to_cart(self, authenticated_user, inventory_page):
        """Test adding multiple items to cart"""
        items_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bike Light",
            "Sauce Labs Bolt T-Shirt",
        ]

        for item in items_to_add:
            inventory_page.add_item_to_cart_by_name(item)

        cart_count = inventory_page.get_cart_badge_count()
        assert cart_count == str(
            len(items_to_add)
        ), f"Expected cart count to be {len(items_to_add)}, but got {cart_count}"

    def test_product_sorting_by_name_az(self, authenticated_user, inventory_page):
        """Test sorting products by name A to Z"""
        inventory_page.sort_products("az")

        item_names = inventory_page.get_item_names()
        sorted_names = sorted(item_names)
        assert item_names == sorted_names, "Products are not sorted alphabetically A-Z"

    def test_product_sorting_by_name_za(self, authenticated_user, inventory_page):
        """Test sorting products by name Z to A"""
        inventory_page.sort_products("za")

        item_names = inventory_page.get_item_names()
        sorted_names = sorted(item_names, reverse=True)
        assert item_names == sorted_names, "Products are not sorted alphabetically Z-A"

    def test_product_sorting_by_price_low_to_high(
        self, authenticated_user, inventory_page
    ):
        """Test sorting products by price low to high"""
        inventory_page.sort_products("lohi")

        prices = inventory_page.get_item_prices()
        price_values = [float(price.replace("$", "")) for price in prices]
        sorted_prices = sorted(price_values)
        assert (
            price_values == sorted_prices
        ), "Products are not sorted by price low to high"

    def test_logout_functionality(self, authenticated_user, inventory_page, login_page):
        """Test logout functionality"""
        inventory_page.logout()

        login_page.verify_login_page_loaded()
        assert (
            "saucedemo.com" in inventory_page.page.url
            and "inventory" not in inventory_page.page.url
        )
