import time
import pytest
from framework.pages.dynamic_content_page import DynamicContentPage


def test_dynamic_content_for_duplicates(browser):
    dynamic_page_url = "http://the-internet.herokuapp.com/dynamic_content"
    dynamic_page = DynamicContentPage(browser)
    dynamic_page.browser.open(dynamic_page_url)
    dynamic_page.wait_for_open()

    timeout = time.time() + 30

    while time.time() < timeout:
        sources = dynamic_page.get_image_sources()
        if len(sources) != len(set(sources)):
            print(f"Найдены дубликаты: {sources}")
            assert True
            return
        browser.driver.refresh()

    pytest.fail("Не удалось найти дубликаты изображений за 30 секунд")
