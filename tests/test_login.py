import pytest
from playwright.sync_api import expect
from utils.test_data import TestData
from pages.login_page import LoginPage  # Adjust if necessary


@pytest.mark.login
class TestLogin:
    """Test cases for the login functionality."""

    def test_blank_username_and_password(self, login_page: LoginPage) -> None:
        """
        Test login attempt with both username and password left blank.

        Args:
            login_page (LoginPage): The login page object.
        """
        login_page.navigate()
        login_page.login("", "")
        assert login_page.is_error_message_visible()
        expect(login_page.page.locator(login_page.ERROR_MESSAGE)).to_have_text(
            "Epic sadface: Username is required"
        )

    def test_blank_username(self, login_page: LoginPage) -> None:
        """
        Test login attempt with blank username.

        Args:
            login_page (LoginPage): The login page object.
        """
        login_page.navigate()
        login_page.login("", TestData.VALID_PASSWORD)
        assert login_page.is_error_message_visible()
        expect(login_page.page.locator(login_page.ERROR_MESSAGE)).to_have_text(
            "Epic sadface: Username is required"
        )

    def test_blank_password(self, login_page: LoginPage) -> None:
        """
        Test login attempt with blank password.

        Args:
            login_page (LoginPage): The login page object.
        """
        login_page.navigate()
        login_page.login(TestData.STANDARD_USER, "")
        assert login_page.is_error_message_visible()
        expect(login_page.page.locator(login_page.ERROR_MESSAGE)).to_have_text(
            "Epic sadface: Password is required"
        )

    def test_valid_login(self, login_page: LoginPage) -> None:
        """
        Test login attempt with valid username and password.

        Args:
            login_page (LoginPage): The login page object.
        """
        login_page.navigate()
        login_page.login(TestData.STANDARD_USER, TestData.VALID_PASSWORD)
        assert "inventory.html" in login_page.page.url

    def test_invalid_login(self, login_page: LoginPage) -> None:
        """
        Test login attempt with invalid password.

        Args:
            login_page (LoginPage): The login page object.
        """
        login_page.navigate()
        login_page.login(TestData.STANDARD_USER, TestData.INVALID_PASSWORD)
        assert login_page.is_error_message_visible()
        expect(login_page.page.locator(login_page.ERROR_MESSAGE)).to_have_text(
            "Epic sadface: Username and password do not match any user in this service"
        )

    def test_locked_out_user(self, login_page: LoginPage) -> None:
        """
        Test login attempt with a locked-out user.

        Args:
            login_page (LoginPage): The login page object.
        """
        login_page.navigate()
        login_page.login(TestData.LOCKED_OUT_USER, TestData.VALID_PASSWORD)
        assert login_page.is_error_message_visible()
        expect(login_page.page.locator(login_page.ERROR_MESSAGE)).to_have_text(
            "Epic sadface: Sorry, this user has been locked out."
        )
