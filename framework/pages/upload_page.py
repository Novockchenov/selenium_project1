from framework.pages.base_page import BasePage
from framework.elements.web_element import WebElement
from framework.elements.button import Button
from framework.utils.pyautogui_utils import PyAutoGuiUtilities


class FileUploadPage(BasePage):
    """Описывает страницу загрузки файлов."""
    UNIQUE_ELEMENT_LOC = "file-upload"
    UPLOAD_INPUT_LOC = "file-upload"
    UPLOAD_BUTTON_LOC = "file-submit"
    DRAG_DROP_AREA_LOC = "drag-drop-upload"
    UPLOADED_FILES_PANEL_LOC = "uploaded-files"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "File Upload Page"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC, "Upload Input")
        self.upload_button = Button(self.browser, self.UPLOAD_BUTTON_LOC, "Upload Button")
        self.drag_drop_area = WebElement(self.browser, self.DRAG_DROP_AREA_LOC, "Drag and Drop Area")
        self.uploaded_files_panel = WebElement(self.browser, self.UPLOADED_FILES_PANEL_LOC, "Uploaded Files Panel")

    def upload_file_with_send_keys(self, file_path: str):
        """Самый надежный способ: отправка пути напрямую в input."""
        self.unique_element.send_keys(file_path)
        self.upload_button.click()

    def upload_file_with_dialog(self, file_path: str):
        """Способ с вызовом системного окна и его обработкой через PyAutoGui."""
        self.drag_drop_area.click()
        PyAutoGuiUtilities.upload_file(file_path)

    def get_uploaded_file_name(self) -> str:
        """Возвращает имя файла из панели успешной загрузки."""
        return self.uploaded_files_panel.get_text()
