from framework.pages.infinity_scroll_page import InfinityScrollPage


def test_infinity_scroll_loads_content(browser):
    scroll_page_url = "http://the-internet.herokuapp.com/infinite_scroll"
    scroll_page = InfinityScrollPage(browser)
    browser.open(scroll_page_url)
    scroll_page.wait_for_open()
    initial_count = scroll_page.get_paragraphs_count()
    scroll_page.scroll_to_load_new_content()
    count_after_scroll = scroll_page.get_paragraphs_count()

    assert count_after_scroll > initial_count, "Количество абзацев не увеличилось после прокрутки"
