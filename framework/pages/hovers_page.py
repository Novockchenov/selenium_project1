from framework.pages.base_page import BasePage
from framework.elements.web_element import WebElement
from framework.elements.multi_web_element import MultiWebElement


class HoversPage(BasePage):
    """Описывает страницу с элементами, появляющимися при наведении."""
    UNIQUE_ELEMENT_LOC = "//div[contains(@class, 'figure')]"
    USER_FIGURES_LOC_TEMPLATE = "//div[contains(@class, 'figure')][{}]"

    USERNAME_LOC_TEMPLATE = "(//div[contains(@class,'figure')])[{}]//h5"
    PROFILE_LINK_LOC_TEMPLATE = "(//div[contains(@class,'figure')])[{}]//a"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Hovers Page"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC, "User Figure")
        self.user_figures = MultiWebElement(self.browser, self.USER_FIGURES_LOC_TEMPLATE, "User Figure")

    def hover_on_user(self, index: int):
        """
        Наводит курсор на аватар пользователя с указанным индексом.
        Вся логика поиска элемента и вызова .move_to() спрятана здесь.
        """
        locator = self.USER_FIGURES_LOC_TEMPLATE.format(index)
        user_figure = WebElement(self.browser, locator, f"User Figure {index}")
        user_figure.move_to()

    def get_username_text(self, index: int) -> str:
        """
        Возвращает имя пользователя в виде строки (str).
        """
        locator = self.USERNAME_LOC_TEMPLATE.format(index)
        username_element = WebElement(self.browser, locator, f"Username for user {index}")
        return username_element.get_text()

    def click_view_profile_link(self, index: int):
        """
        Кликает по ссылке 'View profile' для указанного пользователя.
        """
        locator = self.PROFILE_LINK_LOC_TEMPLATE.format(index)
        profile_link = WebElement(self.browser, locator, f"Profile link for user {index}")
        profile_link.click()
