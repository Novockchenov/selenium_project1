import pytest
from core.webdriver_factory import WebDriverFactory


@pytest.fixture(scope="session")
def driver():
    # Получаем драйвер и используем Singleton
    web_driver = WebDriverFactory.get_driver()

    yield web_driver

    # Этот код выполнится после завершения ВСЕХ тестов (из-за scope="session")
    # Закрываем браузер
    WebDriverFactory.quit_driver()
