from playwright.sync_api import expect

from pages.base_page import BasePage


class ExercisePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.add_cart_blue_top = page.locator('.overlay-content [data-product-id="1"]')
        self.add_cart_men_tshirt = page.locator(
            '.overlay-content [data-product-id="2"]'
        )
        self.continue_shopping = page.get_by_role("button", name="Continue Shopping")
        self.blue_top = (
            page.locator(".single-products").filter(has_text="Blue Top").first
        )
        self.men_tshirt = (
            page.locator(".single-products").filter(has_text="Men Tshirt").first
        )
        self.view_cart = page.get_by_role("link", name="View Cart")

    def add_blue_top(self):
        self.blue_top.hover()
        self.add_cart_blue_top.click()
        self.continue_shopping.click()

    def expect_continue_shopping_closed(self):
        expect(self.continue_shopping).not_to_be_visible()

    def add_menu_tshirt(self):
        self.men_tshirt.hover()
        self.add_cart_men_tshirt.click()
        self.view_cart.click()
