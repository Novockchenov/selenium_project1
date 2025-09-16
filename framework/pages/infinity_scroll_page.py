import time
from framework.logger.logger import Logger
from framework.pages.base_page import BasePage
from framework.elements.multi_web_element import MultiWebElement
from framework.elements.web_element import WebElement


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

    def scroll_to_load_new_content(self, target_count: int):
        """
        Прокручивает страницу вниз в цикле, пока количество абзацев
        не достигнет заданного значения.
        """
        Logger.info(f"Начинаю скролл, пока не будет {target_count} абзацев.")
        timeout = time.time() + 60
        last_known_count = -1

        while self.get_paragraphs_count() < target_count:
            if time.time() > timeout:
                Logger.error(f"Не удалось достичь {target_count} абзацев за 60 секунд.")
                break

            current_count = self.get_paragraphs_count()
            if current_count == last_known_count:
                Logger.warning("Количество абзацев перестало увеличиваться. Прерываю цикл.")
                break
            last_known_count = current_count

            all_paragraphs = list(self.paragraphs)
            if not all_paragraphs:
                break

            last_paragraph = all_paragraphs[-1]
            last_paragraph.scroll_to_element()
