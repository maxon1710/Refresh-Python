from playwright.sync_api import expect

from pages.base_page import BasePage


class ExerciseLogin(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.input_login = page.locator('[data-qa="login-email"]')
        self.input_password = page.locator('[data-qa="login-password"]')
        self.login_button = page.locator('[data-qa="login-button"]')
        self.incorrect_alert = page.get_by_text("Your email or password is incorrect!")
        self.logged_in_as = page.get_by_text("Logged in as")

    def login(self, login: str, password: str):
        self.input_login.fill(login)
        self.input_password.fill(password)
        self.login_button.click()

    def expect_incorrect_alert(self):
        expect(self.incorrect_alert).to_be_visible()
        expect(self.incorrect_alert).to_have_text(
            "Your email or password is incorrect!"
        )

    def expect_logged_in(self):
        expect(self.logged_in_as).to_be_visible()
