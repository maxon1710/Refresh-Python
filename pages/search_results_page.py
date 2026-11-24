from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class ResultSearchDuckGoPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.result_value = page.locator('[name="q"], value')
        self.result_count = page.get_by_test_id("result").nth(4)

    def expect_result_search(self, value: str):
        expect(self.result_value).to_have_value(value)

    def expect_result_count(self):
        expect(self.result_count).to_be_visible()
