from framework.elements.button import Button
from framework.elements.web_element import WebElement
from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AlertsPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//h3[text()='JavaScript Alerts']")
    JS_ALERT_BUTTON_LOC = (By.XPATH, "//button[text()='Click for JS Alert']")
    JS_CONFIRM_BUTTON_LOC = (By.XPATH, "//button[text()='Click for JS Confirm']")
    JS_PROMPT_BUTTON_LOC = (By.XPATH, "//button[text()='Click for JS Prompt']")
    RESULT_TEXT_LOC = (By.ID, "result")

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
