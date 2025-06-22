import os
import sys
import pytest
from playwright.sync_api import Page, sync_playwright

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from pages.login_page import LoginPage


@pytest.fixture(scope='session')
def browser():
    '''
    Fixture to provide a browser instance for tests.
    This uses Playwright to launch a Chromium browser in headless mode.
    '''
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()
        

@pytest.fixture(scope='function')
def context(browser):
    '''
    Fixture to provide a browser context for tests.
    This creates a new browser context for each test session.
    '''
    context = browser.new_context(
        viewport={'width': 1280, 'height': 720},
    )
    yield context
    context.close()
    
@pytest.fixture
def page(context):
    '''
    Fixture to provide a page instance for tests.
    This creates a new page in the browser context for each test.
    '''
    page = context.new_page()
    yield page
    page.close()
    


@pytest.fixture
def login_page(page: Page) :
    '''
    Fixture to navigate to the login page before each test.
    This ensures that the page is ready for testing.
    '''
    return LoginPage(page)

