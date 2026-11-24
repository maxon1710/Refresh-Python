from pages.base_page import BasePage
from pages.litres_popular_page import PopularLitres


class MainLitres(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.box_category = page.get_by_test_id("lowerMenu_items").locator("a")
        self.popular_category = page.get_by_test_id("lowerMenu__item--popular")

    def go_to_popular(self):
        self.popular_category.click()
        return PopularLitres(self.page)

    def get_category(self):
        return self.box_category.all_inner_texts()
