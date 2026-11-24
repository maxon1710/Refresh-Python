from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url)
        self.page.wait_for_load_state("domcontentloaded")
        return self

    def wait_for_page_load(self):
        self.page.wait_for_load_state("networkidle")
        return self
