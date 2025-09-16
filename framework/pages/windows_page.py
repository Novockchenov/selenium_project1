from framework.elements.web_element import WebElement
from framework.pages.base_page import BasePage


class WindowsPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//a[text()='Click Here']"
    CLICK_HERE_LINK_LOC = "//a[text()='Click Here']"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Windows Page"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC, "Click Here Link Presence Marker")
        self.click_here_link = WebElement(self.browser, self.CLICK_HERE_LINK_LOC, "Click Here Link")

    def click_here(self):
        """Выполняет клик по ссылке."""
        self.click_here_link.click()

    def get_link_text(self) -> str:
        """Возвращает текст ссылки 'Click Here'."""
        return self.click_here_link.get_text()


class NewWindowPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//h3[contains(text(), 'New Window')]"
    HEADER_LOC = "//h3[contains(text(), 'New Window')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "New Window Page"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC, "Header")
        self.header = WebElement(self.browser, self.HEADER_LOC, "Header")

    def get_header_text(self) -> str:
        """Возвращает текст заголовка на странице."""
        return self.header.get_text()
