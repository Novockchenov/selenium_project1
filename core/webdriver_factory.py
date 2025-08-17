from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Singleton
class WebDriverFactory:
    _driver = None

    @classmethod
    def get_driver(cls):

        if cls._driver is None:
            chrome_options = Options()

            chrome_options.add_argument("--window-size=1920,1080")

            cls._driver = webdriver.Chrome(options=chrome_options)

        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver is not None:
            cls._driver.quit()
            cls._driver = None
