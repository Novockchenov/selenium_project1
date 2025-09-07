from framework.pages.hovers_page import HoversPage


def test_user_hovers_and_profile_links(browser):
    hovers_page_url = "http://the-internet.herokuapp.com/hovers"
    hovers_page = HoversPage(browser)
    hovers_page.browser.open(hovers_page_url)
    hovers_page.wait_for_open()

    for user_index in range(1, 4):
        current_user_figure = hovers_page.get_user_figure_by_index(user_index)
        current_user_figure.move_to()
        username_element = hovers_page.get_username_for_user(user_index)
        expected_username = f"name: user{user_index}"

        assert username_element.get_text() == expected_username, \
            f"Имя пользователя для юзера {user_index} неверное"
        profile_link = hovers_page.get_profile_link_for_user(user_index)
        profile_link.click()

        assert f"/users/{user_index}" in browser.url, \
            f"Открылась неверная страница профиля для юзера {user_index}"

        browser.driver.back()
