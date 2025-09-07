from selenium.webdriver.common.keys import Keys
from framework.elements.web_element import WebElement
from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SliderPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//input[@type='range']")
    SLIDER_LOC = (By.XPATH, "//input[@type='range']")
    SLIDER_VALUE_LOC = (By.XPATH, "//span[@id='range']")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Slider Page"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC, "Slider")
        self.slider_value = WebElement(self.browser, self.SLIDER_VALUE_LOC, "Slider Value")

    def get_slider_value(self) -> str:
        """Возвращает текущее значение слайдера."""
        return self.slider_value.get_text()

    def set_slider_value(self, target_value: float):
        """Устанавливает значение слайдера, нажимая стрелку вправо."""
        # Сначала получаем текущее значение
        current_value = float(self.get_slider_value())

        # Шаг слайдера на этом сайте - 0.5
        step = 0.5

        # Вычисляем, сколько раз нужно нажать на стрелку
        steps_to_move = int((target_value - current_value) / step)

        if steps_to_move > 0:
            # Отправляем нужное количество нажатий клавиши "стрелка вправо"
            for _ in range(steps_to_move):
                self.unique_element.send_keys(Keys.ARROW_RIGHT)
