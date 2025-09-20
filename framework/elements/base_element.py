from typing import TYPE_CHECKING, Union
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support import expected_conditions
from framework.logger.logger import Logger


if TYPE_CHECKING:
    from framework.browser.browser import Browser


class BaseElement:
    DEFAULT_TIMEOUT = 10

    def __init__(self, browser: 'Browser', locator: Union[str, tuple], description: str = None,
                 timeout: int = DEFAULT_TIMEOUT) -> None:
        self.browser = browser
        self.timeout = timeout
        self.locator = locator
        if isinstance(locator, str):
            if "//" in locator:
                self.locator = (By.XPATH, locator)
            else:
                self.locator = (By.ID, locator)
        self.description = description if description else str(locator)
        self.wait = WebDriverWait(self.browser.driver, timeout=self.timeout)

    def __str__(self) -> str:
        """Строковое представление для логов, например: Button[Кнопка 'Войти']"""
        return f"{self.__class__.__name__}[{self.description}]"

    def _wait_for(self, expected_condition) -> WebElement:
        """Приватный метод-помощник для всех ожиданий."""
        try:
            Logger.info(f"{self}: жду условия {expected_condition.__name__}")
            element = self.wait.until(method=expected_condition(self.locator))
            return element
        except TimeoutException as err:
            Logger.error(f"{self}: не дождался условия за {self.timeout} сек. {err}")
            raise

    def wait_for_presence(self) -> WebElement:
        """Ждет, пока элемент появится в DOM."""
        return self._wait_for(expected_conditions.presence_of_element_located)

    def wait_for_clickable(self) -> WebElement:
        """Ждет, пока элемент станет видимым и кликабельным."""
        return self._wait_for(expected_conditions.element_to_be_clickable)

    def click(self) -> None:
        element = self.wait_for_clickable()
        Logger.info(f"{self}: выполняю клик")
        try:
            element.click()
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def js_click(self) -> None:
        """Выполняет клик с помощью JavaScript."""
        element = self.wait_for_presence()
        Logger.info(f"{self}: выполняю клик через JavaScript")
        try:
            self.browser.execute_script("arguments[0].click();", element)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def context_click(self) -> None:
        """Выполняет клик правой кнопкой мыши по элементу."""
        element = self.wait_for_clickable()
        Logger.info(f"{self}: выполняю контекстный клик")
        try:
            actions = ActionChains(self.browser.driver)
            actions.context_click(element)
            actions.perform()
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def get_text(self) -> str:
        element = self.wait_for_presence()
        Logger.info(f"{self}: получаю текст")
        text = element.text
        Logger.info(f"{self}: текст = '{text}'")
        return text

    def send_keys(self, keys: str) -> None:
        """Отправляет нажатия клавиш в элемент."""
        element = self.wait_for_clickable()
        Logger.info(f"{self}: отправляю клавиши '{keys}'")
        try:
            element.send_keys(keys)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def get_attribute(self, name: str) -> str:
        """
        Возвращает значение атрибута элемента.
        Сначала ждет появления элемента, затем получает атрибут.
        """
        element = self.wait_for_presence()

        Logger.info(f"{self}: получаю атрибут '{name}'")
        try:
            attribute_value = element.get_attribute(name)
            Logger.info(f"{self}: значение атрибута = '{attribute_value}'")
            return attribute_value
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def move_to(self) -> None:
        """Наводит курсор мыши на элемент."""
        element = self.wait_for_presence()
        Logger.info(f"{self}: навожу курсор мыши")
        try:
            actions = ActionChains(self.browser.driver)
            actions.move_to_element(element)
            actions.perform()
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def scroll_to_element(self) -> None:
        """Скроллит страницу до видимости элемента."""
        element = self.wait_for_presence()
        Logger.info(f"{self}: скроллю до элемента")
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)

    def is_exists(self) -> bool:
        """
        Проверяет, существует ли элемент в DOM, не ожидая долго
        и не записывая ошибку в лог в случае отсутствия.
        Возвращает True, если элемент найден, иначе False.
        """
        try:
            wait = WebDriverWait(self.browser.driver, timeout=0)
            wait.until(expected_conditions.presence_of_element_located(self.locator))
            return True
        except TimeoutException:
            return False


