from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from core.config_reader import ConfigReader


class BasePage:
    DEFAULT_WAIT_TIME = ConfigReader.get_wait_time()

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME)
