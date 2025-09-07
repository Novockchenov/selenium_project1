from selenium.webdriver.common.by import By
from framework.pages.base_page import BasePage
from framework.elements.multi_web_element import MultiWebElement
from framework.elements.web_element import WebElement


class InfinityScrollPage(BasePage):
    """Описывает страницу с бесконечной прокруткой."""
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//div[@class='jscroll-inner']")
    PARAGRAPHS_LOC = "//div[@class='jscroll-inner']/div[@class='jscroll-added'][{}]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Infinity Scroll Page"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC, "Content Area")
        self.paragraphs = MultiWebElement(self.browser, self.PARAGRAPHS_LOC, "Paragraph")

    def get_paragraphs_count(self) -> int:
        """Считает количество абзацев на странице."""
        return len(list(self.paragraphs))

    def scroll_down(self):
        """Прокручивает страницу вниз, используя метод нашего браузера."""
        self.browser.scroll_to_bottom()
