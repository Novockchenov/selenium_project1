from framework.pages.context_menu_page import ContextMenuPage


def test_context_menu(browser):
    context_page_url = "http://the-internet.herokuapp.com/context_menu"
    context_page = ContextMenuPage(browser)
    browser.open(context_page_url)
    context_page.wait_for_open()
    context_page.click_hot_spot_area()
    browser.wait_alert_present()
    expected_text = "You selected a context menu"
    actual_text = browser.get_alert_text()
    assert actual_text == expected_text, \
        f"Текст в алерте неверный. Ожидали: '{expected_text}', получили: '{actual_text}'"
    browser.accept_alert()
