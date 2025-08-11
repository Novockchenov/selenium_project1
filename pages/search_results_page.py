from selenium.webdriver.common.by import By
from pages.base_page import BasePage

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import re


class SearchResultsPage(BasePage):
    # Уникальный локатор для контейнера с результатами, чтобы убедиться, что мы на нужной странице
    SEARCH_RESULTS_CONTAINER = (By.XPATH, "//*[@id='search_resultsRows']")
    SORT_BY_DROPDOWN = (By.XPATH, "//*[@id='sort_by_trigger']")
    SORT_BY_PRICE_DESC_OPTION = (By.XPATH, "//*[@id='sort_by_listctn']//a[@id='Price_DESC']")
    SEARCH_RESULT_ROWS = (By.XPATH, "//a[contains(@class, 'search_result_row')]")
    SEARCH_RESULT_TITLE = (By.XPATH, ".//span[@class='title']")  # .// для поиска внутри другого элемента

    # SEARCH_RESULT_PRICE = (By.XPATH, "(//*[ @id='search_resultsRows']//div[contains(concat(' ', normalize-space(@class), ' '), ' discount_final_price ') and contains(concat(' ', normalize-space(@class), ' '), ' your_price ')]//div)[2]")

    # SEARCH_RESULT_PRICE = (By.XPATH,"//*[ @id='search_resultsRows']//div[contains(@class,'discount_final_price')]//div[2]")

    # SEARCH_RESULT_PRICE = (By.XPATH, ".//div[contains(@class,'discount_final_price')]//div[2]")

    SEARCH_RESULT_PRICE = (By.XPATH, ".//div[contains(@class, 'search_price')]")

    def __init__(self, driver):
        super().__init__(driver)
        # Убеждаемся, что мы на странице
        self.find_element(self.SEARCH_RESULTS_CONTAINER)

    def sort_by_price_desc(self):
        # Находим элемент поиска, за которым будем смотреть - за устареванием.
        first_game_before_sort = self.find_element(self.SEARCH_RESULT_ROWS)

        self.find_element(self.SORT_BY_DROPDOWN).click()

        price_desc_option = WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(self.SORT_BY_PRICE_DESC_OPTION)
        )

        price_desc_option.click()

        # Ждём пока старый список не исчезнет!!
        WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME).until(
            EC.staleness_of(first_game_before_sort)
        )

    def get_top_n_prices(self, n: int) -> list[float]:
        """
        Находит N первых игр и возвращает список их цен.
        Надежно обрабатывает товары со скидкой, без скидки и без цены.
        """
        game_rows = self.find_elements(self.SEARCH_RESULT_ROWS)[:n]
        prices = []

        for row in game_rows:
            price_elements = row.find_elements(*self.SEARCH_RESULT_PRICE)

            if price_elements:
                price_text = price_elements[0].text
                print(f"Найден текст цены: '{price_text}'")

                # Ищем ВСЕ числа в тексте
                found_numbers = re.findall(r'(\d+[\.,]?\d*)', price_text)

                if found_numbers:
                    # Если числа найдены, берем ПОСЛЕДНЕЕ из них (это всегда финальная цена)
                    price_str = found_numbers[-1].replace(',', '.')
                    price_as_float = float(price_str)
                    prices.append(price_as_float)
                else:
                    # Блок цены есть, но чисел в нем нет (маловероятно, но возможно)
                    prices.append(0.0)
            else:
                # У товара вообще нет блока с ценой (например, "скоро выйдет")
                print("Элемент с ценой не найден для этого товара. Присвоена цена 0.0")
                prices.append(0.0)

        return prices
