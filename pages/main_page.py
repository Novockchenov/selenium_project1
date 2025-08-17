from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from core.config_reader import ConfigReader
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# import config

class MainPage(BasePage):
    STEAM_URL = "https://store.steampowered.com/"

    SEARCH_INPUT = (By.ID, "store_nav_search_term")

    CAROUSEL = (By.XPATH, "//*[contains(@class, 'carousel_container')]")

    def __init__(self, driver):
        super().__init__(driver)

    def search_for_game(self, query: str):
        wait = WebDriverWait(self.driver, ConfigReader.get_wait_time())
        search_field = wait.until(EC.element_to_be_clickable(self.SEARCH_INPUT))
        search_field.clear()
        search_field.send_keys(query)
        search_field.submit()
