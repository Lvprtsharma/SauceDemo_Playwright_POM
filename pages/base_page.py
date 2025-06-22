from playwright.sync_api import Page, expect
from abc import ABC, abstractmethod

class BasePage(ABC):
    '''
    Base class for all pages in the application.
    Provides common functionality for page interactions.
    '''
    
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url: str):
        '''
        Navigate to the specified URL.
        '''
        self.page.goto(url)
        self.page.wait_for_load_state('networkidle')
        expect(self.page).to_have_url(url)
        
    def get_title(self) -> str:
        '''
        Get the title of the current page.
        '''
        return self.page.title()
    
    def wait_for_element(self, selector: str, timeout: int = 5000):
        '''
        Wait for an element to be present on the page.
        '''
        self.page.wait_for_selector(selector, timeout=timeout)
        
    def click_element(self, selector: str):
        '''
        Click on an element specified by the selector.
        '''
        self.wait_for_element(selector)
        self.page.click(selector)
    
    def fill_input(self, selector: str, value: str):
        '''
        Fill an input field with the specified value.
        '''
        self.wait_for_element(selector)
        self.page.fill(selector, value)
        
    def get_text(self, selector: str) -> str:
        '''
        Get the text content of an element specified by the selector.
        '''
        self.wait_for_element(selector)
        return self.page.text_content(selector)
    
    def is_element_visible(self, selector: str) -> bool:
        '''
        Check if an element is visible on the page.
        '''
        try:
            self.page.wait_for_selector(selector, state='visible', timeout=1000)
            return True
        except Exception:
            return False
        
