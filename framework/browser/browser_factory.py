from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from framework.logger.logger import Logger
from enum import Enum
import platform

if platform.system() == "Windows":
    HEADLESS_MODE: bool = True
else:  # Linux / Docker
    HEADLESS_MODE: bool = True


class AvailableDriverName(Enum):
    CHROME = "chrome"


class BrowserFactory:
    @staticmethod
    def get_driver(driver_name: AvailableDriverName = AvailableDriverName.CHROME,
                   extra_options: list[str] = None) -> WebDriver:

        common_flags = [
            "--disable-gpu",
            "--window-size=1920,1080",
        ]

        if driver_name == AvailableDriverName.CHROME:
            chrome_options = webdriver.ChromeOptions()

            for flag in common_flags:
                chrome_options.add_argument(flag)

            if platform.system() == "Windows":
                platform_flags = [
                    "--headless",
                ]
            else:  # Linux / Docker
                platform_flags = [
                    "--headless=new",
                    "--no-sandbox",
                    "--disable-dev-shm-usage",
                ]

            for flag in platform_flags:
                chrome_options.add_argument(flag)

            if extra_options:
                for opt in extra_options:
                    chrome_options.add_argument(opt)

            Logger.info(f"Запуск webdriver '{driver_name.value}' с опциями: {chrome_options.arguments}")

            driver = webdriver.Chrome(options=chrome_options)
            return driver

        else:
            raise NotImplementedError(f"Драйвер '{driver_name.value}' не реализован")
