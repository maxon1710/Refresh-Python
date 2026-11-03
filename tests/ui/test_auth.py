import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage

load_dotenv()


@pytest.mark.ui
def test_login_page(page: Page):
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    username = os.getenv("SAUCE_USERNAME_VALID")
    password = os.getenv("SAUCE_PASSWORD")
    login_page.login(username, password)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


@pytest.mark.ui
def test_blocked_client(page: Page):
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    username = os.getenv("SAUCE_USERNAME_LOCKED")
    password = os.getenv("SAUCE_PASSWORD")
    login_page.login(username, password)
    login_page.expect_locked_out_error()
