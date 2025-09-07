from framework.pages.frames_page import FramesMainPage, NestedFramesPage


def test_nested_frames(browser):
    frames_url = "http://the-internet.herokuapp.com/frames"
    main_page = FramesMainPage(browser)
    main_page.browser.open(frames_url)
    main_page.go_to_nested_frames()
    nested_page = NestedFramesPage(browser)
    nested_page.wait_for_open()
    browser.switch_to_frame(nested_page.frame_top)
    browser.switch_to_frame(nested_page.frame_left)
    left_text = nested_page.get_text_from_body()

    assert left_text == "LEFT", "Неверный текст в левом фрейме"

    browser.switch_to_default_content()
    browser.switch_to_frame(nested_page.frame_top)
    browser.switch_to_default_content()
    browser.switch_to_frame(nested_page.frame_bottom)
    bottom_text = nested_page.get_text_from_body()

    assert bottom_text == "BOTTOM", "Неверный текст в нижнем фрейме"

    browser.switch_to_default_content()
