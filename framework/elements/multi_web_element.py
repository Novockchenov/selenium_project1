from typing_extensions import Self
from framework.browser.browser import Browser
from framework.elements.web_element import WebElement


class MultiWebElement:
    DEFAULT_TIMEOUT = 20

    def __init__(
            self,
            browser: Browser,
            formattable_xpath: str,
            description: str = None,
            timeout: int = None,
    ) -> None:
        self.index = 1
        self.browser = browser
        self.formattable_xpath = formattable_xpath
        self.timeout = timeout if timeout is not None else self.DEFAULT_TIMEOUT
        self.description = description if description else self.formattable_xpath.format("*")

    def __iter__(self) -> Self:
        """Метод, который вызывается в начале цикла for."""
        self.index = 1
        return self

    def __next__(self) -> WebElement:
        """Метод, который вызывается на каждой итерации цикла for."""
        current_element = WebElement(
            self.browser,
            self.formattable_xpath.format(self.index),
            f"{self.description}[{self.index}]",
            timeout=self.timeout,
        )
        if not current_element.is_exists():
            raise StopIteration
        else:
            self.index += 1
            return current_element

    def __str__(self) -> str:
        return f"{self.__class__.__name__}[{self.description}]"

    def __repr__(self) -> str:
        return str(self)
