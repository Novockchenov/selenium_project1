import pytest
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from core.config_reader import ConfigReader


@pytest.mark.parametrize("game_name, num_results_to_check", [
    ("The Witcher", 10),
    ("Fallout", 20)
])
def test_game_search_and_sort(driver, game_name, num_results_to_check):
    base_url = ConfigReader.get_base_url()
    driver.get(base_url)

    main_page = MainPage(driver)
    main_page.search_for_game(game_name)

    search_results_page = SearchResultsPage(driver)
    search_results_page.wait_for_page_load()
    search_results_page.sort_by_price_desc()

    prices = search_results_page.get_top_n_prices(num_results_to_check)

    expected_sorted_prices = sorted(prices, reverse=True)

    assert prices == expected_sorted_prices, \
        (f"Сортировка по убыванию цены работает некорректно. "
         f"Ожидаемый порядок (отсортированный): {expected_sorted_prices} "
         f"Фактический порядок со страницы:     {prices}")
