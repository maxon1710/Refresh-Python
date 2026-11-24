from playwright.sync_api import Page

from pages.base_page import BasePage


class SearchDuckGoPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.search_input = page.locator('[name="q"]')

    def search(self, query: str):
        self.search_input.fill(query)
        self.search_input.press("Enter")
