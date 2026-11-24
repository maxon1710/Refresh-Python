import os

from dotenv import load_dotenv
from playwright.sync_api import expect

from pages.login_page import LoginPage

load_dotenv()


def test_saucedemo_products(page):
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    username = os.getenv("SAUCE_USERNAME_VALID")
    password = os.getenv("SAUCE_PASSWORD")
    login_page.login(username, password)
    name_product = page.locator('[data-test="inventory-item-name"]')

    actual = []
    for product in name_product.all():
        text = product.inner_text().strip()
        actual.append(text)

    expected = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt"]
    assert set(expected).issubset(set(actual))


def test_add_jacket_via_parent(page):
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    username = os.getenv("SAUCE_USERNAME_VALID")
    password = os.getenv("SAUCE_PASSWORD")
    login_page.login(username, password)
    jacket = page.locator('[data-test="inventory-item-name"]').filter(
        has_text="Sauce Labs Fleece Jacket"
    )
    box_jacket = jacket.locator("../../..")
    add_to_card_jacket = box_jacket.get_by_role("button", name="Add to cart")
    add_to_card_jacket.click()
    cart = page.locator('[data-test="shopping-cart-link"]')
    expect(cart).to_have_text("1")
