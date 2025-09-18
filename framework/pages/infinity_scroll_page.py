import time
from framework.logger.logger import Logger
from framework.pages.base_page import BasePage
from framework.elements.multi_web_element import MultiWebElement
from framework.elements.web_element import WebElement
from selenium.webdriver.support.ui import WebDriverWait


class InfinityScrollPage(BasePage):
    """Описывает страницу с бесконечной прокруткой."""
    UNIQUE_ELEMENT_LOC = "//div[contains(@class, 'jscroll-inner')]"
    PARAGRAPHS_LOC = "(//div[contains(@class, 'jscroll-inner')]/div)[{}]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Infinity Scroll Page"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC, "Content Area")
        self.paragraphs = MultiWebElement(self.browser, self.PARAGRAPHS_LOC, "Paragraph")

    def get_paragraphs_count(self) -> int:
        """Считает количество абзацев на странице."""
        return len(list(self.paragraphs))

    def wait_for_new_paragraphs(self, old_count: int, timeout: int = 5):
        """Явное ожидание появления хотя бы одного нового параграфа."""
        WebDriverWait(self.browser.driver, timeout).until(
            lambda _: self.get_paragraphs_count() > old_count,
            message="Не появились новые параграфы"
        )

    def scroll_to_load_new_content(self, target_count: int):
        """
        Прокручивает страницу вниз в цикле, пока количество абзацев
        не достигнет заданного значения или не исчерпано время/попытки.
        """
        Logger.info(f"Начинаю скролл, пока не будет {target_count} абзацев.")
        timeout = time.time() + 60
        last_known_count = self.get_paragraphs_count()
        attempts_without_increase = 0
        max_attempts_without_increase = 3

        while self.get_paragraphs_count() < target_count:
            if time.time() > timeout:
                Logger.error(f"Не удалось достичь {target_count} абзацев за 60 секунд.")
                break

            current_count = self.get_paragraphs_count()
            all_paragraphs = list(self.paragraphs)

            if not all_paragraphs:
                Logger.warning("Абзацы на странице не найдены. Завершаю скролл.")
                break

            last_paragraph = all_paragraphs[-1]
            # last_paragraph.scroll_to_element()
            self.browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)

            try:
                self.wait_for_new_paragraphs(current_count, timeout=5)
            except Exception:
                attempts_without_increase += 1
                Logger.warning(f"Новые параграфы не появились (попытка {attempts_without_increase}).")
                if attempts_without_increase >= max_attempts_without_increase:
                    Logger.warning("Количество абзацев перестало увеличиваться. Прерываю цикл.")
                    break
            else:
                attempts_without_increase = 0
                Logger.info(f"Количество абзацев увеличилось: {current_count} → {self.get_paragraphs_count()}")

            last_known_count = self.get_paragraphs_count()
