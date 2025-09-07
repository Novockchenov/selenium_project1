from framework.pages.windows_page import WindowsPage, NewWindowPage


def test_window_handles(browser):
    windows_page_url = "http://the-internet.herokuapp.com/windows"
    windows_page = WindowsPage(browser)
    windows_page.browser.open(windows_page_url)
    windows_page.wait_for_open()
    windows_page.click_here()
    browser.switch_to_window("New Window")
    new_window_page = NewWindowPage(browser)
    new_window_page.wait_for_open()

    assert new_window_page.get_header_text() == "New Window", "Неверный заголовок на новой вкладке"

    browser.close()
    browser.switch_to_default_window()
    windows_page.wait_for_open()

    assert "Click Here" in windows_page.unique_element.get_text(), "Не удалось вернуться на главную страницу"
