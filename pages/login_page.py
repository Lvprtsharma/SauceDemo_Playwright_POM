import os
from dotenv import load_dotenv
from playwright.sync_api import expect

load_dotenv()

from .base_page import BasePage


class LoginPage(BasePage):

    """
    Locator for the login page elements.
    """

    USERNAME_INPUT = '[data-test="username"]'
    PASSWORD_INPUT = '[data-test="password"]'
    LOGIN_BUTTON = '[data-test="login-button"]'
    ERROR_MESSAGE = '[data-test="error"]'
    LOGIN_LOGO = ".login_logo"

    def __init__(self, page):
        super().__init__(page)
        self.url = os.getenv("LOGIN_URL")

    def navigate(self):
        """
        Navigate to the login page.
        """
        self.page.goto(self.url)
        expect(self.page).to_have_url(os.getenv("LOGIN_URL"))

    def enter_username(self, username):
        """
        Enter the username in the username input field.
        """
        self.page.fill(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        """
        Enter the password in the password input field.
        """
        self.page.fill(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        """
        Click the login button.
        """
        self.page.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        """
        Perform the login action with the provided username and password.
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def get_error_message(self):
        """
        Get the error message displayed on the login page.
        """
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_message_visible(self):
        """
        Check if the error message is visible on the login page.
        """
        return self.is_element_visible(self.ERROR_MESSAGE)

    def verify_login_logo(self):
        """
        Verify that the login logo is visible on the login page.
        """
        return self.is_element_visible(self.LOGIN_LOGO)
