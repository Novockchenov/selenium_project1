from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from framework.logger.logger import Logger
from enum import Enum
import platform


class AvailableDriverName(Enum):
    CHROME = "chrome"
    FIREFOX = "firefox"


class BrowserFactory:
    @staticmethod
    def get_driver(driver_name: AvailableDriverName = AvailableDriverName.CHROME,
                   extra_options: list[str] = None) -> WebDriver:
        if driver_name == AvailableDriverName.CHROME:
            chrome_options = webdriver.ChromeOptions()

            if platform.system() == "Windows":
                default_flags = [
                    "--headless",
                    "--disable-gpu",
                    "--window-size=1920,1080",
                ]
            else:  # Linux / Docker
                default_flags = [
                    "--headless=new",
                    "--no-sandbox",
                    "--disable-dev-shm-usage",
                    "--disable-gpu",
                    "--window-size=1920,1080",
                    "--user-data-dir=/tmp/chrome-profile"
                ]

            for flag in default_flags:
                chrome_options.add_argument(flag)

            if extra_options:
                for opt in extra_options:
                    chrome_options.add_argument(opt)

            Logger.info(f"Запуск webdriver '{driver_name.value}' с опциями: {chrome_options.arguments}")

            return webdriver.Chrome(options=chrome_options)

        elif driver_name == AvailableDriverName.FIREFOX:
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument("--headless")
            if extra_options:
                for opt in extra_options:
                    firefox_options.add_argument(opt)
            Logger.info(f"Запуск webdriver '{driver_name.value}' с опциями: {firefox_options.arguments}")
            return webdriver.Firefox(options=firefox_options)

        else:
            raise NotImplementedError(f"Драйвер '{driver_name.value}' не реализован")
