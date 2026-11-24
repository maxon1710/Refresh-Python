import os

from dotenv import load_dotenv
from playwright.sync_api import Page

from pages.catalog_page import CatalogPage

load_dotenv()


def test_add_product_in_backpack(logged_in_page: Page):
    catalog_page = CatalogPage(logged_in_page)
    catalog_page.goto("https://www.saucedemo.com/inventory.html")
    catalog_page.add_backpack_to_cart()
    catalog_page.expect_cart_in_badge("1")
    cart_page = catalog_page.open_cart()
    cart_page.expect_item_cart("Sauce Labs Backpack")


def test_remove_product(logged_in_page: Page):
    catalog_page = CatalogPage(logged_in_page)
    catalog_page.goto("https://www.saucedemo.com/inventory.html")
    catalog_page.add_backpack_to_cart()
    catalog_page.expect_cart_in_badge("1")
    cart_page = catalog_page.open_cart()
    cart_page.expect_item_cart("Sauce Labs Backpack")
    cart_page.remove_backpack()
    cart_page.expect_item_not_in_card()


def test_order_zakaz(logged_in_page: Page):
    catalog_page = CatalogPage(logged_in_page)
    catalog_page.goto("https://www.saucedemo.com/inventory.html")
    catalog_page.add_backpack_to_cart()
    catalog_page.expect_cart_in_badge("1")
    cart_page = catalog_page.open_cart()
    cart_page.expect_item_cart("Sauce Labs Backpack")
    checkout_page = cart_page.checkout_in_cart()
    checkout_page.expect_checkout()
    checkout_overview_page = checkout_page.date_in_form_checkout(
        os.getenv("FIRST_NAME"), os.getenv("LAST_NAME"), os.getenv("ZIP_CODE")
    )
    checkout_complete_page = checkout_overview_page.finish_order()
    checkout_complete_page.expect_complete_order()
