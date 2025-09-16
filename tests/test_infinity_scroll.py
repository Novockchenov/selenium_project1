from framework.pages.infinity_scroll_page import InfinityScrollPage

TARGET_PARAGRAPH_COUNT = 4


def test_infinity_scroll_loads_content(browser):
    scroll_page_url = "http://the-internet.herokuapp.com/infinite_scroll"
    scroll_page = InfinityScrollPage(browser)
    browser.open(scroll_page_url)
    scroll_page.wait_for_open()
    scroll_page.scroll_to_load_new_content(TARGET_PARAGRAPH_COUNT)
    final_count = scroll_page.get_paragraphs_count()

    assert final_count >= TARGET_PARAGRAPH_COUNT, \
        f"Ожидалось как минимум {TARGET_PARAGRAPH_COUNT} абзацев, но найдено только {final_count}"
