from playwright.sync_api import expect

from pages.base_page import BasePage


class ExercisePayment(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.heading_payment = page.get_by_role("heading", name="Payment")
        self.name_on_card = page.locator('input[name="name_on_card"]')
        self.card_number = page.locator('input[name="card_number"]')
        self.cvc = page.get_by_role("textbox", name="ex.")
        self.expiration = page.get_by_role("textbox", name="MM")
        self.yyyy = page.get_by_role("textbox", name="YYYY")
        self.pay_and_confirm_order = page.get_by_role(
            "button", name="Pay and Confirm Order"
        )

    def expect_payment_page(self):
        expect(self.heading_payment).to_be_visible()

    def input_data_for_payment(self):
        self.name_on_card.fill("Max Maximov")
        self.card_number.fill("0123-4567-8910-1112")
        self.cvc.fill("666")
        self.expiration.fill("03")
        self.yyyy.fill("2028")

    def click_pay_and_confirm(self):
        self.pay_and_confirm_order.click()
