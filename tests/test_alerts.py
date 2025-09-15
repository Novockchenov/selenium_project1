import random
import string
from framework.pages.alerts_page import AlertsPage


def test_alerts(browser):
    alerts_page_url = "https://the-internet.herokuapp.com/javascript_alerts"
    alerts_page = AlertsPage(browser)
    alerts_page.browser.open(alerts_page_url)
    alerts_page.wait_for_open()

    alerts_page.click_for_js_alert()
    browser.wait_alert_present()
    alert_text = browser.get_alert_text()
    assert alert_text == "I am a JS Alert", "Неверный текст в JS Alert"
    browser.accept_alert()
    assert alerts_page.get_result_text() == "You successfully clicked an alert", "Неверный результат после JS Alert"

    alerts_page.click_for_js_confirm()
    browser.wait_alert_present()
    alert_text = browser.get_alert_text()
    assert alert_text == "I am a JS Confirm", "Неверный текст в JS Confirm"
    browser.accept_alert()
    assert alerts_page.get_result_text() == "You clicked: Ok", "Неверный результат после JS Confirm"

    random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    alerts_page.js_prompt_button.click()
    browser.wait_alert_present()
    alert_text = browser.get_alert_text()
    assert alert_text == "I am a JS prompt", "Неверный текст в JS Prompt"
    browser.send_keys_to_alert(random_text)
    browser.accept_alert()
    assert alerts_page.get_result_text() == f"You entered: {random_text}", "Неверный результат после JS Prompt"


def test_alerts_with_js_click(browser):
    alerts_page_url = "https://the-internet.herokuapp.com/javascript_alerts"
    alerts_page = AlertsPage(browser)
    alerts_page.browser.open(alerts_page_url)
    alerts_page.wait_for_open()

    alerts_page.click_for_js_alert()
    browser.wait_alert_present()
    browser.accept_alert()
    assert "You successfully clicked an alert" in alerts_page.get_result_text()

    alerts_page.click_for_js_confirm()
    browser.wait_alert_present()
    browser.accept_alert()
    assert "You clicked: Ok" in alerts_page.get_result_text()
