from playwright.sync_api import expect
from pages.checkout_page import CheckoutPage
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.inventory_item = page.locator('[data-test="inventory-item-name"]')
        self.remove_item = page.locator('[data-test="remove-sauce-labs-backpack"]')
        self.checkout_button = page.locator('[data-test="checkout"]')

    def expect_item_cart(self, name: str):
        expect(self.inventory_item).to_have_text(name)

    def expect_remove_cart(self, name: str):
        expect(self.remove_item).to_have_text(name)

    def remove_backpack(self):
        self.remove_item.click()

    def expect_item_not_in_card(self):
        expect(self.inventory_item).not_to_be_visible()

    def checkout_in_cart(self):
        self.checkout_button.click()
        return CheckoutPage(self.page)
