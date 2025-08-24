from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from core.config_reader import ConfigReader
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# import config

class MainPage(BasePage):
    SEARCH_INPUT = (By.ID, "store_nav_search_term")

    CAROUSEL = (By.XPATH, "//*[contains(@class, 'carousel_container')]")

    def wait_for_page_load(self):
        self.wait.until(EC.visibility_of_element_located(self.CAROUSEL))

    def search_for_game(self, query: str):
        search_field = self.wait.until(EC.element_to_be_clickable(self.SEARCH_INPUT))
        search_field.clear()
        search_field = self.wait.until(EC.element_to_be_clickable(self.SEARCH_INPUT))
        search_field.send_keys(query)
        search_field.submit()
