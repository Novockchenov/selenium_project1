from framework.pages.basic_auth_page import BasicAuthPage


def test_basic_auth(browser):
    auth_url = "http://admin:admin@the-internet.herokuapp.com/basic_auth"
    basic_auth_page = BasicAuthPage(browser)
    browser.open(auth_url)
    basic_auth_page.wait_for_open()
    success_message = basic_auth_page.get_success_message()
    expected_message = "Congratulations! You must have the proper credentials."

    assert success_message == expected_message, "Сообщение об успехе неверное или отсутствует"
