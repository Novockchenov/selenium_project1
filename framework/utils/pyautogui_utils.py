import time
import pyautogui
from framework.logger.logger import Logger


class PyAutoGuiUtilities:
    @staticmethod
    def upload_file(file_path: str) -> None:
        Logger.info(f"Обрабатываю системное окно для загрузки файла")
        time.sleep(3)
        Logger.debug(f"Ввожу путь к файлу '{file_path}' в окно выбора файла")
        pyautogui.typewrite(file_path)
        Logger.debug("Нажимаю 'Enter' для подтверждения выбора")
        pyautogui.hotkey("enter")
        time.sleep(3)
