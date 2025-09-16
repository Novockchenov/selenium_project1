from selenium.webdriver.common.keys import Keys
from framework.elements.web_element import WebElement
from framework.pages.base_page import BasePage


class SliderPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//input[@type='range']"
    SLIDER_LOC = "//input[@type='range']"
    SLIDER_VALUE_LOC = "//span[@id='range']"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Slider Page"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC, "Slider Presence Marker")
        self.slider = WebElement(self.browser, self.SLIDER_LOC, "Slider")
        self.slider_value = WebElement(self.browser, self.SLIDER_VALUE_LOC, "Slider Value")

    def get_slider_value(self) -> str:
        """Возвращает текущее значение слайдера."""
        return self.slider_value.get_text()

    def get_slider_step(self) -> float:
        return float(self.slider.get_attribute("step"))

    def set_slider_value(self, target_value: float):
        """Устанавливает значение слайдера, нажимая стрелку вправо."""
        current_value = float(self.get_slider_value())
        step = self.get_slider_step()
        steps_to_move = int((target_value - current_value) / step)

        if steps_to_move > 0:
            for _ in range(steps_to_move):
                self.slider.send_keys(Keys.ARROW_RIGHT)

    def get_slider_min_value(self) -> float:
        return float(self.slider.get_attribute("min"))

    def get_slider_max_value(self) -> float:
        return float(self.slider.get_attribute("max"))
