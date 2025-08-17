import pytest
from core.webdriver_factory import WebDriverFactory


@pytest.fixture(scope="function")
def driver():
    # Получаем драйвер и используем Singleton
    web_driver = WebDriverFactory.get_driver()

    yield web_driver

    WebDriverFactory.quit_driver()
