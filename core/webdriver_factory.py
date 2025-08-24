from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from core.config_reader import ConfigReader


class WebDriverFactory:
    """Управления единственным экземпляром WebDriver на основе Singleton."""
    _driver = None

    @classmethod
    def get_driver(cls):

        if cls._driver is None:
            chrome_options = Options()
            options = ConfigReader.get_driver_options()
            for option in options:
                chrome_options.add_argument(option)
            cls._driver = webdriver.Chrome(options=chrome_options)
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver is not None:
            cls._driver.quit()
            cls._driver = None
