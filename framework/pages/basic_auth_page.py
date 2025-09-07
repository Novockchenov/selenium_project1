from framework.elements.web_element import WebElement
from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class BasicAuthPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//p[contains(text(), 'Congratulations')]")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Basic Auth Page"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC, "Success Message")

    def get_success_message(self) -> str:
        """Возвращает текст сообщения об успешной авторизации."""
        return self.unique_element.get_text()
