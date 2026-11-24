import re

from playwright.sync_api import expect

from pages.base_page import BasePage


class ExerciseOrderPlaced(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.order_placed = page.get_by_text("Order Placed! Congratulations")

    def expect_order_placed(self):
        expect(self.order_placed).to_be_visible()

    def expect_url_order_placed(self):
        expect(self.page).to_have_url(re.compile(r".*payment_done"))
