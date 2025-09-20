import time
import pyautogui
from framework.logger.logger import Logger


class PyAutoGuiUtilities:
    @staticmethod
    def upload_file(file_path: str) -> None:
        Logger.info("Обрабатываю системное окно для загрузки файла")
        time.sleep(2)
        time.sleep(1)
        pyautogui.typewrite(file_path, interval=0.05)
        Logger.debug(f"Введен путь к файлу '{file_path}'")
        time.sleep(1)
        pyautogui.press('enter')
        Logger.debug("Нажата клавиша Enter для подтверждения выбора файла.")
        time.sleep(2)
