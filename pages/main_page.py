from selenium.webdriver.common.by import By
from pages.base_page import BasePage
#import config

class MainPage(BasePage):

    STEAM_URL = "https://store.steampowered.com/"

    SEARCH_INPUT = (By.XPATH, "//*[@id='store_nav_search_term']")

    # уникальный элемент главной страницы для ожидания загрузки
    CAROUSEL = (By.XPATH, "//*[contains(@class, 'carousel_container')]")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        super().open(self.STEAM_URL)
        # Ждем, пока загрузится уникальный элемент именно главной страницы!!
        self.find_element(self.CAROUSEL)

    def search_for_game(self, query: str):
        search_field = self.find_element(self.SEARCH_INPUT)
        search_field.clear()
        search_field.send_keys(query)
        search_field.submit()  # Эмулирует нажатие Enter, переходя на страницу результатов