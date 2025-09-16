from framework.elements.web_element import WebElement
from framework.pages.base_page import BasePage


class ContextMenuPage(BasePage):
    UNIQUE_ELEMENT_LOC = "hot-spot"
    HOT_SPOT_AREA_LOC = "hot-spot"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Context Menu Page"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC, "Hot Spot Area Presence Marker")
        self.hot_spot_area = WebElement(self.browser, self.HOT_SPOT_AREA_LOC, "Hot Spot Area")

    def click_hot_spot_area(self):
        """Кликает ПКМ по выделенной области."""
        self.hot_spot_area.context_click()
