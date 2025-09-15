from framework.elements.button import Button
from framework.elements.web_element import WebElement
from framework.pages.base_page import BasePage


class AlertsPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//h3[text()='JavaScript Alerts']"
    JS_ALERT_BUTTON_LOC = "//button[text()='Click for JS Alert']"
    JS_CONFIRM_BUTTON_LOC = "//button[text()='Click for JS Confirm']"
    JS_PROMPT_BUTTON_LOC = "//button[text()='Click for JS Prompt']"
    RESULT_TEXT_LOC = "result"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Alerts Page"

        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC, "Header")
        self.js_alert_button = Button(self.browser, self.JS_ALERT_BUTTON_LOC, "JS Alert Button")
        self.js_confirm_button = Button(self.browser, self.JS_CONFIRM_BUTTON_LOC, "JS Confirm Button")
        self.js_prompt_button = Button(self.browser, self.JS_PROMPT_BUTTON_LOC, "JS Prompt Button")
        self.result_text = WebElement(self.browser, self.RESULT_TEXT_LOC, "Result Text")

    def get_result_text(self) -> str:
        """Возвращает текст из поля Result."""
        return self.result_text.get_text()

    def click_for_js_alert(self):
        """Кликает по кнопке 'Click for JS Alert'."""
        self.js_alert_button.click()

    def click_for_js_confirm(self):
        """Кликает по кнопке 'Click for JS Confirm'."""
        self.js_confirm_button.click()
