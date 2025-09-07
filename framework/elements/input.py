from framework.elements.base_element import BaseElement
from framework.logger.logger import Logger


class Input(BaseElement):

    def clear(self) -> None:
        element = self.wait_for_visible()
        Logger.info(f"{self}: очищаю поле")
        element.clear()

    def send_keys(self, keys: str, clear: bool = True) -> None:
        if clear:
            self.clear()

        element = self.wait_for_visible()
        Logger.info(f"{self}: ввожу текст '{keys}'")
        element.send_keys(keys)
