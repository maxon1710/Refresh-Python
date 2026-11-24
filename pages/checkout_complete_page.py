from playwright.sync_api import expect

from pages.base_page import BasePage


class CheckoutComplete(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.title_complete = page.locator('[data-test="complete-header"]')

    def expect_complete_order(self):
        expect(self.title_complete).to_have_text("Thank you for your order!")
