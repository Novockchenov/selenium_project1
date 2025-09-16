from framework.elements.web_element import WebElement
from framework.pages.base_page import BasePage


class BasicAuthPage(BasePage):
    SUCCESS_MESSAGE_LOC = "//p[contains(text(), 'Congratulations')]"
    UNIQUE_ELEMENT_LOC = "//p[contains(text(), 'Congratulations')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Basic Auth Page"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC, "Success Message")
        self.success_message_label = WebElement(self.browser, self.SUCCESS_MESSAGE_LOC, "Success Message Label")

    def get_success_message(self) -> str:
        """Возвращает текст сообщения об успешной авторизации."""
        return self.success_message_label.get_text()
