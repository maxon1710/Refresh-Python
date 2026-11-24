from playwright.sync_api import expect

from pages.base_page import BasePage


class ExerciseCheckout(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.checkout_address_details = page.get_by_role(
            "heading", name="Address Details"
        )
        self.comment = page.locator('textarea[name="message"]')
        self.place_order = page.get_by_role("link", name="Place Order")

    def expect_address_details(self):
        expect(self.checkout_address_details).to_be_visible()

    def input_comments(self):
        self.comment.fill("Тестовый заказ")

    def click_place_order(self):
        self.place_order.click()
