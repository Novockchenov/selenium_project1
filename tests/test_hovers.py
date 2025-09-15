from framework.pages.hovers_page import HoversPage


def test_user_hovers_and_profile_links(browser):
    hovers_page_url = "http://the-internet.herokuapp.com/hovers"
    hovers_page = HoversPage(browser)
    browser.open(hovers_page_url)
    hovers_page.wait_for_open()

    for user_index in range(1, 4):
        hovers_page.hover_on_user(user_index)

        actual_username = hovers_page.get_username_text(user_index)
        expected_username = f"name: user{user_index}"

        assert actual_username == expected_username, \
            f"Имя пользователя неверное. Ожидали: '{expected_username}', получили: '{actual_username}'"

        hovers_page.click_view_profile_link(user_index)

        assert f"/users/{user_index}" in browser.url, \
            f"Открылась неверная страница профиля для юзера {user_index}"

        browser.driver.back()
