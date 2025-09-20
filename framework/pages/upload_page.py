import time

from selenium.webdriver import ActionChains

from framework.pages.base_page import BasePage
from framework.elements.web_element import WebElement
from framework.elements.button import Button
from framework.utils.pyautogui_utils import PyAutoGuiUtilities


class FileUploadPage(BasePage):
    """Описывает страницу загрузки файлов."""
    UNIQUE_ELEMENT_LOC = "file-upload"
    UPLOAD_INPUT_LOC = "file-upload"
    UPLOAD_BUTTON_LOC = "file-submit"
    CHOOSE_FILE_LABEL_LOC = "file-upload"
    UPLOADED_FILES_PANEL_LOC = "uploaded-files"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "File Upload Page"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC, "Upload Input")
        self.upload_button = Button(self.browser, self.UPLOAD_BUTTON_LOC, "Upload Button")
        self.choose_file_label = WebElement(self.browser, self.CHOOSE_FILE_LABEL_LOC, "Choose File Label")
        self.uploaded_files_panel = WebElement(self.browser, self.UPLOADED_FILES_PANEL_LOC, "Uploaded Files Panel")

    def upload_file_with_send_keys(self, file_path: str):
        """Самый надежный способ: отправка пути напрямую в input."""
        self.unique_element.send_keys(file_path)
        self.upload_button.js_click()

    def upload_file_with_dialog4(self, file_path: str):
        """Способ с вызовом системного окна и его обработкой через PyAutoGui."""
        try:
            self.unique_element.js_click()  # self.choose_file_label.click()
        except Exception:
            self.unique_element.js_click()  # self.choose_file_label.js_click()
        PyAutoGuiUtilities.upload_file(file_path)
        self.upload_button.click()

    def upload_file_with_dialog(self, file_path: str):

        el = self.choose_file_label.wait_for_clickable()
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)

        try:
            ActionChains(self.browser.driver).move_to_element(el).pause(0.1).click(el).perform()
        except Exception:

            el = self.choose_file_label.wait_for_clickable()
            el.click()

        time.sleep(0.3)

        PyAutoGuiUtilities.upload_file(file_path)

        self.upload_button.click()

    def get_uploaded_file_name(self) -> str:
        """Возвращает имя файла из панели успешной загрузки."""
        return self.uploaded_files_panel.get_text()
