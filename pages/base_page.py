from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    DEFAULT_WAIT_TIME = 15

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    # Используем константу по умолчанию, но оставляем возможность ее переопределить
    def find_element(self, locator, time=DEFAULT_WAIT_TIME):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, time=DEFAULT_WAIT_TIME):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))
