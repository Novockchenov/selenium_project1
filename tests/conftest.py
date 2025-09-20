import os
import pytest
from framework.browser.browser_factory import BrowserFactory
from framework.browser.browser import Browser
from framework.logger.logger import Logger


@pytest.fixture
def browser():
    Logger.info("===== Тест начался =====")
    driver = BrowserFactory.get_driver()
    browser_instance = Browser(driver)
    browser_instance.driver.maximize_window()
    yield browser_instance
    browser_instance.quit()
    Logger.info("===== Тест завершен =====")


@pytest.fixture
def temp_file():
    file_name = "test_upload_file.txt"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("Это файл для автоматизации")
    file_path = os.path.abspath(file_name)
    yield file_path
    os.remove(file_path)
