from framework.pages.slider_page import SliderPage


def test_slider(browser):
    slider_page_url = "http://the-internet.herokuapp.com/horizontal_slider"
    slider_page = SliderPage(browser)
    slider_page.browser.open(slider_page_url)
    slider_page.wait_for_open()
    target_value = 3.5
    slider_page.set_slider_value(target_value)
    assert float(slider_page.get_slider_value()) == target_value, "Значение слайдера установлено неверно"
