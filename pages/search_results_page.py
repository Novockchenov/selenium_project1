from selenium.webdriver.common.by import By
from pages.base_page import BasePage

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.price_parser import PriceParser

import re


class SearchResultsPage(BasePage):
    SEARCH_RESULTS_CONTAINER = (By.ID, "search_resultsRows")
    SORT_BY_DROPDOWN = (By.ID, "sort_by_trigger")
    SORT_BY_PRICE_DESC_OPTION = (By.ID, "Price_DESC")
    SEARCH_RESULT_ROWS = (By.XPATH, "//a[contains(@class, 'search_result_row')]")
    SEARCH_RESULT_TITLE = (By.XPATH, ".//span[@class='title']")

    SEARCH_RESULT_PRICE = (By.XPATH, ".//div[contains(@class, 'search_price')]")

    ALL_PRICES_IN_ROWS = (By.XPATH, "//a[contains(@class, 'search_result_row')]//div[contains(@class, 'search_price')]")

    LOADING_OVERLAY = (By.ID, "search_results_loading")

    def wait_for_page_load(self):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_RESULTS_CONTAINER))

    def sort_by_price_desc(self):
        dropdown = self.wait.until(EC.element_to_be_clickable(self.SORT_BY_DROPDOWN))
        dropdown.click()

        price_desc_option = self.wait.until(EC.element_to_be_clickable(self.SORT_BY_PRICE_DESC_OPTION))
        price_desc_option.click()

        self.wait.until(EC.invisibility_of_element_located(self.LOADING_OVERLAY))

    def get_top_n_prices(self, n: int) -> list[float]:
        """
        Находит N первых игр и возвращает список их цен.
        Надежно обрабатывает товары со скидкой, без скидки и без цены.
        """
        wait = WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME)

        all_price_elements = wait.until(EC.presence_of_all_elements_located(self.ALL_PRICES_IN_ROWS))[:n]

        prices = []
        for price_element in all_price_elements:
            price_as_float = PriceParser.parse_price(price_element.text)
            prices.append(price_as_float)
        return prices
