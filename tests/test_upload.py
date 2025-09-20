import os

import pytest

from framework.pages.upload_page import FileUploadPage
from framework.browser.browser_factory import HEADLESS_MODE


def test_simple_file_upload(browser, temp_file):
    upload_page_url = "http://the-internet.herokuapp.com/upload"
    upload_page = FileUploadPage(browser)
    browser.open(upload_page_url)
    upload_page.wait_for_open()
    upload_page.upload_file_with_send_keys(temp_file)

    assert upload_page.get_uploaded_file_name() == os.path.basename(temp_file), "Имя загруженного файла неверное"


@pytest.mark.skipif(HEADLESS_MODE, reason="Диалоговое окно загрузки не работает в headless режиме")
def test_upload_with_dialog_window(browser, temp_file):
    # if browser.driver.is_headless:
    #     pytest.skip("Диалоговое окно не работает в headless режиме")

    upload_page_url = "http://the-internet.herokuapp.com/upload"
    upload_page = FileUploadPage(browser)
    browser.open(upload_page_url)
    upload_page.wait_for_open()
    upload_page.upload_file_with_dialog(temp_file)

    uploaded_name = upload_page.get_uploaded_file_name()
    expected_name = os.path.basename(temp_file)

    assert uploaded_name == expected_name, f"Ожидалось '{expected_name}', получено '{uploaded_name}'"

