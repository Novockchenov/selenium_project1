import time
from framework.pages.dynamic_content_page import DynamicContentPage


def test_dynamic_content_for_duplicates(browser):
    dynamic_page_url = "http://the-internet.herokuapp.com/dynamic_content"
    dynamic_page = DynamicContentPage(browser)
    browser.open(dynamic_page_url)
    dynamic_page.wait_for_open()

    timeout = time.time() + 30
    duplicates_found = False

    while time.time() < timeout:
        sources = dynamic_page.get_image_sources()
        if len(sources) != len(set(sources)):
            print(f"Найдены дубликаты: {sources}")
            duplicates_found = True
            break
        browser.driver.refresh()

    assert duplicates_found, "Не удалось найти дубликаты изображений за 30 секунд"
