from pages.litres_main_page import MainLitres


def test_litres_drill(page):
    main_page_litres = MainLitres(page)
    page.goto("https://www.litres.ru/")
    expected = ["Новинки", "Популярное", "100 лучших книг"]
    actual = main_page_litres.get_category()
    assert set(expected).issubset(set(actual))
