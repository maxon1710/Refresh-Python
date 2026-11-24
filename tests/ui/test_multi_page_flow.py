from playwright.sync_api import expect

from pages.litres_main_page import MainLitres


def test_multi_page_flow(page):
    main_litres = MainLitres(page)
    page.goto("https://www.litres.ru/")
    main_litres.go_to_popular()
    expect(page).to_have_url("https://www.litres.ru/popular/")
