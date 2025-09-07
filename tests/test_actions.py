from framework.pages.context_menu_page import ContextMenuPage


def test_context_menu(browser):
    context_page_url = "http://the-internet.herokuapp.com/context_menu"
    context_page = ContextMenuPage(browser)
    context_page.browser.open(context_page_url)
    context_page.wait_for_open()
    context_page.click_hot_spot_area()
    browser.wait_alert_present()
    alert_text = browser.get_alert_text()
    assert alert_text == "You selected a context menu", "Неверный текст в алерте"
    browser.accept_alert()
