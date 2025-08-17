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
    PRICE_DESC_SORT_URL_PARAM = "sort_by=Price_DESC"
    SEARCH_RESULT_ROWS = (By.XPATH, "//a[contains(@class, 'search_result_row')]")
    SEARCH_RESULT_TITLE = (By.XPATH, ".//span[@class='title']")

    SEARCH_RESULT_PRICE = (By.XPATH, ".//div[contains(@class, 'search_price')]")

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_page_load(self):

        wait = WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME)
        wait.until(EC.visibility_of_element_located(self.SEARCH_RESULTS_CONTAINER))
        return self

    def sort_by_price_desc(self):

        wait = WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME)

        dropdown = wait.until(EC.element_to_be_clickable(self.SORT_BY_DROPDOWN))
        dropdown.click()

        price_desc_option = WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(self.SORT_BY_PRICE_DESC_OPTION)
        )

        price_desc_option.click()

        WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME).until(
            EC.url_contains(self.PRICE_DESC_SORT_URL_PARAM)
        )

    def get_top_n_prices(self, n: int) -> list[float]:
        """
        Находит N первых игр и возвращает список их цен.
        Надежно обрабатывает товары со скидкой, без скидки и без цены.
        """
        wait = WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME)

        game_rows = wait.until(EC.presence_of_all_elements_located(self.SEARCH_RESULT_ROWS))[:n]

        prices = []

        for row in game_rows:
            price_elements = row.find_elements(*self.SEARCH_RESULT_PRICE)

            if price_elements:
                price_text = price_elements[0].text
                price_as_float = PriceParser.parse_price(price_text)
                prices.append(price_as_float)
            else:

                prices.append(0.0)
        return prices
