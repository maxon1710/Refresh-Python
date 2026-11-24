from pages.base_page import BasePage
from pages.checkout_complete_page import CheckoutComplete


class CheckoutOverview(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.backpack = page.locator('[data-test="inventory-item-name"]')
        self.finish = page.locator('[data-test="finish"]')

    def finish_order(self):
        self.finish.click()
        return CheckoutComplete(self.page)
