import random
import string
from framework.pages.alerts_page import AlertsPage


def test_alerts(browser):
    alerts_page_url = "https://the-internet.herokuapp.com/javascript_alerts"
    alerts_page = AlertsPage(browser)
    browser.open(alerts_page_url)
    alerts_page.wait_for_open()
    alerts_page.click_for_js_alert()
    browser.wait_alert_present()
    expected_alert_text = "I am a JS Alert"
    actual_alert_text = browser.get_alert_text()
    assert actual_alert_text == expected_alert_text, \
        f"Текст в JS Alert неверный. Ожидали: '{expected_alert_text}', получили: '{actual_alert_text}'"

    browser.accept_alert()
    expected_result = "You successfully clicked an alert"
    actual_result = alerts_page.get_result_text()
    assert actual_result == expected_result, \
        f"Результат после JS Alert неверный. Ожидали: '{expected_result}', получили: '{actual_result}'"

    alerts_page.click_for_js_confirm()
    expected_alert_text = "I am a JS Confirm"
    browser.wait_alert_present()
    actual_alert_text = browser.get_alert_text()
    assert actual_alert_text == expected_alert_text, \
        f"Текст в JS Confirm неверный. Ожидали: '{expected_alert_text}', получили: '{actual_alert_text}'"

    browser.accept_alert()
    expected_result = "You clicked: Ok"
    actual_result = alerts_page.get_result_text()
    assert actual_result == expected_result, \
        f"Результат после JS Confirm неверный. Ожидали: '{expected_result}', получили: '{actual_result}'"

    random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    alerts_page.js_prompt_button.click()
    browser.wait_alert_present()
    expected_alert_text = "I am a JS prompt"
    actual_alert_text = browser.get_alert_text()
    assert actual_alert_text == expected_alert_text, \
        f"Текст в JS Prompt неверный. Ожидали: '{expected_alert_text}', получили: '{actual_alert_text}'"

    browser.send_keys_to_alert(random_text)
    browser.accept_alert()
    expected_result = f"You entered: {random_text}"
    actual_result = alerts_page.get_result_text()
    assert actual_result == expected_result, \
        f"Результат после JS Prompt неверный. Ожидали: '{expected_result}', получили: '{actual_result}'"


def test_alerts_with_js_click(browser):
    alerts_page_url = "https://the-internet.herokuapp.com/javascript_alerts"
    alerts_page = AlertsPage(browser)
    browser.open(alerts_page_url)
    alerts_page.wait_for_open()
    alerts_page.click_for_js_alert()
    browser.wait_alert_present()
    browser.accept_alert()
    expected_text = "You successfully clicked an alert"
    actual_text = alerts_page.get_result_text()
    assert expected_text in actual_text, \
        f"Ожидалось, что в тексте '{actual_text}' будет подстрока '{expected_text}'"

    alerts_page.click_for_js_confirm()
    browser.wait_alert_present()
    browser.accept_alert()
    expected_text = "You clicked: Ok"
    actual_text = alerts_page.get_result_text()
    assert expected_text in actual_text, \
        f"Ожидалось, что в тексте '{actual_text}' будет подстрока '{expected_text}'"
