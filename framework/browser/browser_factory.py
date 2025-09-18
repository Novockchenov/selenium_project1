from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from framework.logger.logger import Logger
from enum import Enum


class AvailableDriverName(Enum):
    CHROME = "chrome"
    FIREFOX = "firefox"


class BrowserFactory:
    @staticmethod
    def get_driver(driver_name: AvailableDriverName = AvailableDriverName.CHROME,
                   options: list[str] = None) -> WebDriver:
        if options is None:
            options = []
        Logger.info(f"Запуск webdriver '{driver_name.value}' с опциями '{options}'")
        if driver_name == AvailableDriverName.CHROME:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--headless=new")  # без графики
            chrome_options.add_argument("--no-sandbox")  # нужно в Docker
            chrome_options.add_argument("--disable-dev-shm-usage")  # уменьшает проблемы с /dev/shm
            chrome_options.add_argument("--disable-gpu")  # иногда помогает на headless
            chrome_options.add_argument("--user-data-dir=/tmp/chrome-profile")
            for option in options:
                chrome_options.add_argument(option)
            driver = webdriver.Chrome(options=chrome_options)
            return driver
        else:
            raise NotImplementedError(f"Драйвер '{driver_name.value}' не реализован")
