from selenium.webdriver.common.by import By
from framework.pages.base_page import BasePage
from framework.elements.web_element import WebElement
from framework.elements.multi_web_element import MultiWebElement


class HoversPage(BasePage):
    """Описывает страницу с элементами, появляющимися при наведении."""
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//div[@class='figure']")
    USER_FIGURES_LOC_TEMPLATE = "//div[@class='figure'][{}]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Hovers Page"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC, "User Figure")
        self.user_figures = MultiWebElement(self.browser, self.USER_FIGURES_LOC_TEMPLATE, "User Figure")

    def get_user_figure_by_index(self, index: int) -> WebElement:
        """
        Находит и возвращает конкретный WebElement аватара по его номеру (1, 2 или 3).
        """
        locator = (By.XPATH, self.USER_FIGURES_LOC_TEMPLATE.format(index))
        return WebElement(self.browser, locator, f"User Figure {index}")

    def get_username_for_user(self, index: int) -> WebElement:
        """
        Находит и возвращает элемент с именем пользователя,
        который появляется при наведении на аватар с указанным индексом.
        """
        locator = (By.XPATH, f"{self.USER_FIGURES_LOC_TEMPLATE.format(index)}//h5")
        return WebElement(self.browser, locator, f"Username for user {index}")

    def get_profile_link_for_user(self, index: int) -> WebElement:
        """
        Находит и возвращает ссылку "View profile" для пользователя
        с указанным индексом.
        """
        locator = (By.XPATH, f"{self.USER_FIGURES_LOC_TEMPLATE.format(index)}//a")
        return WebElement(self.browser, locator, f"Profile link for user {index}")
