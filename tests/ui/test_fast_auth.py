from playwright.sync_api import expect, Page


def test_open_catalog_directory(logged_in_page: Page):
    # Прыгаем сразу в каталог — формы логина вообще нет в коде!
    logged_in_page.goto("https://www.saucedemo.com/inventory.html")

    # Проверяем, что нас пустило и заголовок 'Products' на экране2
    title = logged_in_page.locator('[data-test="title"]')
    expect(title).to_have_text("Products")
