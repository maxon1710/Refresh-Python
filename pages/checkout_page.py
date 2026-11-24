from playwright.sync_api import expect

from pages.base_page import BasePage
from pages.checkout_overview_page import CheckoutOverview


class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.checkout_info = page.locator('[data-test="title"]')
        self.first_name = page.locator('[data-test="firstName"]')
        self.last_name = page.locator('[data-test="lastName"]')
        self.zip_code = page.locator('[data-test="postalCode"]')
        self.next_continue = page.locator('[data-test="continue"]')

    def expect_checkout(self):
        expect(self.checkout_info).to_have_text("Checkout: Your Information")

    def date_in_form_checkout(self, first_name: str, last_name: str, zip_code: str):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.zip_code.fill(zip_code)
        self.next_continue.click()
        return CheckoutOverview(self.page)
