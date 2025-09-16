from framework.pages.frames_page import FramesMainPage, NestedFramesPage


def test_nested_frames(browser):
    frames_url = "http://the-internet.herokuapp.com/frames"
    main_page = FramesMainPage(browser)
    browser.open(frames_url)
    main_page.go_to_nested_frames()
    nested_page = NestedFramesPage(browser)
    nested_page.wait_for_open()
    browser.switch_to_frame(nested_page.frame_top)
    browser.switch_to_frame(nested_page.frame_left)

    expected_text = "LEFT"
    actual_text = nested_page.get_text_from_body()
    assert actual_text == expected_text, \
        f"Неверный текст в левом фрейме. Ожидали: '{expected_text}', получили: '{actual_text}'"

    browser.switch_to_default_content()
    browser.switch_to_frame(nested_page.frame_top)
    browser.switch_to_default_content()
    browser.switch_to_frame(nested_page.frame_bottom)

    expected_text_bottom = "BOTTOM"
    actual_text_bottom = nested_page.get_text_from_body()
    assert actual_text_bottom == expected_text_bottom, \
        f"Неверный текст в нижнем фрейме. Ожидали: '{expected_text}', получили: '{actual_text}'"

    browser.switch_to_default_content()
