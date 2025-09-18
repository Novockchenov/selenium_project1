import time

from framework.pages.base_page import BasePage
from framework.elements.web_element import WebElement
from framework.elements.button import Button
from framework.utils.pyautogui_utils import PyAutoGuiUtilities


class FileUploadPage(BasePage):
    """Описывает страницу загрузки файлов."""
    UNIQUE_ELEMENT_LOC = "file-upload"
    UPLOAD_INPUT_LOC = "file-upload"
    UPLOAD_BUTTON_LOC = "file-submit"
    CHOOSE_FILE_LABEL_LOC = "*[@id='file-upload']"
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
        self.upload_button.click()

    def upload_file_with_dialog3(self, file_path: str):
        """Загружает файл через системный диалог и PyAutoGui.
           Работает только с GUI (НЕ headless).
        """
        # Используем js_click(), потому что обычный .click()
        # на <input type=file> упрётся в InvalidArgumentException.
        self.unique_element.js_click()

        # Теперь PyAutoGui вводит путь к файлу в открывшийся диалог.
        PyAutoGuiUtilities.upload_file(file_path)

        # Жмём кнопку Upload (это уже Selenium)
        self.upload_button.click()

    def upload_file_with_dialog(self, file_path: str):
        """Способ с вызовом системного окна и его обработкой через PyAutoGui."""
        self.choose_file_label.js_click()  # click()  # ← Это откроет диалог!
        PyAutoGuiUtilities.upload_file(file_path)
        self.upload_button.click()

    def get_uploaded_file_name(self) -> str:
        """Возвращает имя файла из панели успешной загрузки."""
        return self.uploaded_files_panel.get_text()
