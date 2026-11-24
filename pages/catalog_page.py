from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.cart_page import CartPage


class CatalogPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.backpack_add_button = page.locator(
            '[data-test="add-to-cart-sauce-labs-backpack"]'
        )
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')

    def add_backpack_to_cart(self):
        self.backpack_add_button.click()

    def expect_cart_in_badge(self, count):
        expect(self.cart_badge).to_have_text(count)

    def open_cart(self):
        self.cart_link.click()
        return CartPage(self.page)
