def test_category_items(page):
    page.goto("https://automationexercise.com/")
    category = page.get_by_text("Category").locator("..")

    actual = []
    for item in category.locator(".panel-title a").all():
        text = item.inner_text().strip()
        actual.append(text)

    expected = ["WOMEN", "KIDS"]
    print(actual)
    assert set(expected).issubset(set(actual))
