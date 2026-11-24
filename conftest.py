import pytest
from playwright.sync_api import Browser, Page


@pytest.fixture
def logged_in_page(browser: Browser) -> Page:
    # Создаём контекст браузера сразу с куками из файла:
    context = browser.new_context(storage_state="auth.json")
    page = context.new_page()

    yield page

    # Подчищаем за собой (Teardown):
    context.close()
