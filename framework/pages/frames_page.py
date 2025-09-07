from framework.pages.base_page import BasePage
from framework.elements.web_element import WebElement
from selenium.webdriver.common.by import By


class FramesMainPage(BasePage):
    """
    Эта страница описывает стартовую страницу "Frames",
    с которой можно перейти на "Nested Frames" или "iFrame".
    """
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//a[contains(text(), 'Nested Frames')]")
    NESTED_FRAMES_LINK_LOC = (By.XPATH, "//a[contains(text(), 'Nested Frames')]")
    IFRAME_LINK_LOC = (By.XPATH, "//a[contains(text(), 'iFrame')]")

    def __init__(self, browser: "Browser"):
        super().__init__(browser)
        self.page_name = "Frames Main Page"
        self.unique_element = WebElement(
            self.browser, self.UNIQUE_ELEMENT_LOC, "Nested Frames Link"
        )
        self.nested_frames_link = self.unique_element
        self.iframe_link = WebElement(
            self.browser, self.IFRAME_LINK_LOC, "iFrame Link"
        )

    def go_to_nested_frames(self) -> None:
        """Кликает по ссылке, чтобы перейти на страницу с вложенными фреймами."""
        self.nested_frames_link.click()

    def go_to_iframe(self) -> None:
        """Кликает по ссылке, чтобы перейти на страницу с iFrame."""
        self.iframe_link.click()


class NestedFramesPage(BasePage):
    """
    Эта страница описывает страницу с вложенными фреймами (top, bottom, left и т.д.).
    Она содержит элементы, которые являются самими тегами <frame>.
    """
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//frame[@name='frame-top']")
    FRAME_TOP_LOC = (By.XPATH, "//frame[@name='frame-top']")
    FRAME_BOTTOM_LOC = (By.XPATH, "//frame[@name='frame-bottom']")
    FRAME_LEFT_LOC = (By.XPATH, "//frame[@name='frame-left']")
    FRAME_MIDDLE_LOC = (By.XPATH, "//frame[@name='frame-middle']")
    BODY_LOC = (By.XPATH, "//body")

    def __init__(self, browser: "Browser"):
        super().__init__(browser)
        self.page_name = "Nested Frames Page"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC, "Top Frame")
        self.frame_top = self.unique_element
        self.frame_bottom = WebElement(self.browser, self.FRAME_BOTTOM_LOC, "Bottom Frame")
        self.frame_left = WebElement(self.browser, self.FRAME_LEFT_LOC, "Left Frame")
        self.frame_middle = WebElement(self.browser, self.FRAME_MIDDLE_LOC, "Middle Frame")
        self.body = WebElement(self.browser, self.BODY_LOC, "Body of current frame")

    def get_text_from_body(self) -> str:
        """
        Возвращает текст из тела текущего фрейма, на который переключен WebDriver.
        """
        return self.body.get_text()
