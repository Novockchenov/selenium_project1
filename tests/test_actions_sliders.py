from framework.pages.slider_page import SliderPage
import random


def test_slider(browser):
    slider_page_url = "http://the-internet.herokuapp.com/horizontal_slider"
    slider_page = SliderPage(browser)
    browser.open(slider_page_url)
    slider_page.wait_for_open()
    min_val = slider_page.get_slider_min_value()
    max_val = slider_page.get_slider_max_value()
    step = slider_page.get_slider_step()
    possible_values = [min_val + i * step for i in range(int((max_val - min_val) / step) + 1)]
    target_value = random.choice(possible_values)
    slider_page.set_slider_value(target_value)

    actual_value = float(slider_page.get_slider_value())
    assert actual_value == target_value, \
        f"Значение слайдера установлено неверно. Ожидали: {target_value}, получили: {actual_value}"
