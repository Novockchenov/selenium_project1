from framework.pages.windows_page import WindowsPage, NewWindowPage


def test_window_handles(browser):
    windows_page_url = "http://the-internet.herokuapp.com/windows"
    windows_page = WindowsPage(browser)
    browser.open(windows_page_url)
    windows_page.wait_for_open()
    windows_page.click_here()
    browser.switch_to_window("New Window")
    new_window_page = NewWindowPage(browser)
    new_window_page.wait_for_open()

    expected_header = "New Window"
    actual_header = new_window_page.get_header_text()
    assert actual_header == expected_header, \
        f"Заголовок на новой вкладке неверный.\nОжидали: '{expected_header}'\nПолучили: '{actual_header}'"

    browser.close()
    browser.switch_to_default_window()
    windows_page.wait_for_open()
    expected_substring = "Click Here"
    actual_full_text = windows_page.get_link_text()

    assert expected_substring in actual_full_text, \
        f"Не удалось вернуться на главную страницу.\nОжидали найти подстроку '{expected_substring}' " \
        f"в тексте '{actual_full_text}'"
