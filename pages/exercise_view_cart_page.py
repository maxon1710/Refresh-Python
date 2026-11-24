from playwright.sync_api import expect

from pages.base_page import BasePage


class ExerciseViewCart(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.proceed_to_checkout = page.get_by_text("Proceed To Checkout")
        self.button_home = page.get_by_role("link", name="Home", exact=True)
        self.button_cart = page.get_by_role("link", name="Cart")

    def expect_proceed_to_checkout(self):
        expect(self.proceed_to_checkout).to_be_visible()

    def click_home(self):
        self.button_home.click()

    def click_cart(self):
        self.button_cart.click()

    def proceed_checkout(self):
        self.proceed_to_checkout.click()
