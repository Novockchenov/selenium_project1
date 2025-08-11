from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Singleton
class WebDriverFactory:
    _driver = None  # Единственный экземпляр

    @classmethod
    def get_driver(cls):
        # Если экземпляр драйвера еще не создан
        if cls._driver is None:
            print("Создан новый драйвер")

            chrome_options = Options()
            # chrome_options.add_argument("--headless") # Для фонового режима
            chrome_options.add_argument("--window-size=1920,1080")

            # Создаем новый экземпляр и сохраняем его в переменной класса
            cls._driver = webdriver.Chrome(options=chrome_options)

        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver is not None:
            print("Выходим из драйвера")
            cls._driver.quit()
            cls._driver = None  # Сбрасываем, чтобы при следующем запуске создался новый
