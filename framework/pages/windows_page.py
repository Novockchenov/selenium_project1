from framework.elements.web_element import WebElement
from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class WindowsPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//a[text()='Click Here']")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Windows Page"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC, "Click Here Link")

    def click_here(self):
        self.unique_element.click()


class NewWindowPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//h3[contains(text(), 'New Window')]")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "New Window Page"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC, "Header")

    def get_header_text(self) -> str:
        return self.unique_element.get_text()
