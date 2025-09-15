from framework.elements.multi_web_element import MultiWebElement
from framework.pages.base_page import BasePage
from framework.elements.web_element import WebElement


class DynamicContentPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//div[contains(@class, 'large-2')]/img"
    IMAGES_LOC = "(//div[contains(@class, 'large-2')]/img)[{}]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Dynamic Content Page"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC, "Content Image")
        self.images = MultiWebElement(self.browser, self.IMAGES_LOC, "Content Image")

    def get_image_sources(self) -> list[str]:
        """Возвращает список URL-адресов (атрибутов src) всех изображений."""
        sources = []
        for image in self.images:
            sources.append(image.get_attribute("src"))
        return sources
