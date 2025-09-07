import os
from framework.pages.upload_page import FileUploadPage


def test_simple_file_upload(browser, temp_file):
    upload_page_url = "http://the-internet.herokuapp.com/upload"
    upload_page = FileUploadPage(browser)
    upload_page.browser.open(upload_page_url)
    upload_page.wait_for_open()
    upload_page.upload_file_with_send_keys(temp_file)

    assert upload_page.get_uploaded_file_name() == os.path.basename(temp_file), "Имя загруженного файла неверное"


def test_upload_with_dialog_window(browser, temp_file):
    upload_page_url = "http://the-internet.herokuapp.com/upload"
    upload_page = FileUploadPage(browser)
    upload_page.browser.open(upload_page_url)
    upload_page.wait_for_open()
    upload_page.upload_file_with_dialog(temp_file)

    assert upload_page.get_uploaded_file_name() == os.path.basename(
        temp_file), "Имя файла не появилось после загрузки через диалог"
