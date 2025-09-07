from framework.elements.web_element import WebElement
from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ContextMenuPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='hot-spot']")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Context Menu Page"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC, "Context Menu Area")

    def click_hot_spot_area(self):
        """Кликает ПКМ по выделенной области."""
        self.unique_element.context_click()
