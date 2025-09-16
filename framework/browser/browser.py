from typing import TYPE_CHECKING
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import WebDriverException
import time
from selenium.webdriver.remote.webdriver import WebDriver
from framework.logger.logger import Logger

if TYPE_CHECKING:
    from framework.elements.base_element import BaseElement


class Browser:
    DEFAULT_TIMEOUT = 10
    PAGE_LOAD_TIMEOUT = 10

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.driver.set_page_load_timeout(self.PAGE_LOAD_TIMEOUT)
        self.main_handle = None
        self.wait = WebDriverWait(self.driver, timeout=self.DEFAULT_TIMEOUT)

    @property
    def url(self) -> str:
        return self.driver.current_url

    def open(self, url: str) -> None:
        Logger.info(f"url: get {url}")
        try:
            self.driver.get(url)
        except WebDriverException as err:
            Logger.error(f"{err}")
            raise
        self.main_handle = self.driver.current_window_handle

    def close(self) -> None:
        Logger.info(f"close window {self.driver.current_window_handle}")
        self.driver.close()

    def quit(self) -> None:
        Logger.info(f"quit")
        try:
            self.driver.quit()
        except WebDriverException as err:
            Logger.error(f"{err}")
            raise

    def execute_script(self, script: str, *args) -> None:
        Logger.info(f"execute script with args: {args}")
        self.driver.execute_script(script, *args)

    def save_screenshot(self, filename: str) -> None:
        Logger.info(f"save screenshot in {filename}")
        self.driver.save_screenshot(filename)

    def switch_to_default_window(self) -> None:
        Logger.info(f"switch to default window")
        try:
            self.driver.switch_to.window(self.main_handle)
        except WebDriverException as err:
            Logger.error(f"{err}")
            raise ValueError(f"window with handle '{self.main_handle}' wasn't found")

    def switch_to_window(self, title: str) -> None:
        Logger.info(f"switch to window with title '{title}'")
        end_time = time.time() + self.PAGE_LOAD_TIMEOUT
        while time.time() < end_time:
            for handle in self.driver.window_handles:
                self.driver.switch_to.window(handle)
                if self.driver.title == title:
                    Logger.info(f"new window handle is {self.driver.current_window_handle}")
                    return
            time.sleep(1)
        Logger.error(f"window with title '{title}' wasn't found")
        raise ValueError(f"window with title '{title}' wasn't found")

    def wait_alert_present(self) -> None:
        Logger.info(f"wait alert present")
        self.wait.until(expected_conditions.alert_is_present())

    def get_alert_text(self) -> str:
        self.wait_alert_present()
        Logger.info(f"get alert text")
        alert = self.driver.switch_to.alert
        return alert.text

    def accept_alert(self) -> None:
        self.wait_alert_present()
        Logger.info(f"accept alert")
        self.driver.switch_to.alert.accept()

    def send_keys_to_alert(self, text: str) -> None:
        self.wait_alert_present()
        Logger.info(f"Отправляю текст '{text}' в алерт")
        try:
            self.driver.switch_to.alert.send_keys(text)
        except WebDriverException as err:
            Logger.error(f"{err}")
            raise

    def switch_to_frame(self, frame: "BaseElement") -> None:
        Logger.info(f"Переключаюсь на фрейм: {frame}")
        element_to_switch = frame.wait_for_presence()
        self.driver.switch_to.frame(element_to_switch)

    def switch_to_default_content(self) -> None:
        """Возвращает фокус из фрейма на основную страницу."""
        Logger.info("Переключаюсь на основной контент страницы")
        try:
            self.driver.switch_to.default_content()
        except WebDriverException as err:
            Logger.error(f"{err}")
            raise

    def scroll_to_bottom(self) -> None:
        """Прокручивает страницу до самого низа."""
        Logger.info("Выполняю прокрутку страницы вниз")
        try:
            self.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        except WebDriverException as err:
            Logger.error(f"{err}")
            raise

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id='{self.driver.session_id}')"

    def __repr__(self) -> str:
        return str(self)
