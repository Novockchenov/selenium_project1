from framework.browser.browser import Browser
from framework.logger.logger import Logger
from typing import ClassVar, Optional, Union


class BasePage:
    UNIQUE_ELEMENT_LOC: ClassVar[Optional[Union[tuple, str]]] = None

    def __init__(self, browser: Browser):
        self.browser = browser
        self.page_name = "Имя страницы не задано"
        self.unique_element = None

    def wait_for_open(self) -> None:
        """Ждет, пока появится уникальный элемент, подтверждая, что страница загружена."""
        Logger.info(f"{self}: ожидаю открытия страницы")
        self.unique_element.wait_for_presence()

    def __str__(self) -> str:
        """Строковое представление, например: SteamPage[Steam page]"""
        return f"{self.__class__.__name__}[{self.page_name}]"
