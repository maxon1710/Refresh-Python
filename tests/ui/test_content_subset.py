def test_feature_items(page):
    page.goto("https://automationexercise.com/")
    section = page.get_by_text("Features Items").locator("..")

    # Подцель 2: внутри box собираем названия всех <p> в список actual
    actual = []
    for card_title in section.locator(".productinfo p").all():
        text = card_title.inner_text().strip()
        actual.append(text)

    expected = ["Blue Top", "Men Tshirt", "Stylish Dress"]
    print(actual)
    assert set(expected).issubset(set(actual))
