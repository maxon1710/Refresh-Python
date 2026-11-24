import pytest

from pages.duck_duck_go_page import SearchDuckGoPage
from pages.search_results_page import ResultSearchDuckGoPage


@pytest.mark.ui
@pytest.mark.parametrize(
    "query",
    ["qa", "aqa", "python"],
    ids=["Result: QA", "Result: AQA", "Result: Python"],
)
def test_duck_search(page, query):
    search_duck = SearchDuckGoPage(page)
    result_search = ResultSearchDuckGoPage(page)
    search_duck.goto("https://duckduckgo.com/")
    search_duck.search(query)
    result_search.expect_result_search(query)
    result_search.expect_result_count()
