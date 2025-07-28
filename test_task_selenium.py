gimport pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_steam(driver):
    driver.get("https://store.steampowered.com/")

    wait = WebDriverWait(driver, 15)

    login_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "global_action_link")))

    assert login_button.is_displayed()  # , "Кнопка Войти не загрузилась"

    login_button.click()

    username = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type = "text"]')))

    username.is_displayed()

    password = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')

    username.click()
    username.send_keys("PetrovIvanIvanovic")
    username.send_keys(Keys.TAB)

    password.click()
    password.send_keys("123Retefjuiphf")
    password.send_keys(Keys.TAB)

    button_signin = wait.until(
        EC.element_to_be_clickable((By.XPATH,
                                    "//*[@id='responsive_page_template_content']//button[@type='submit']"))
    )

    button_signin.click()

    # class="DjSvCZoKKfoNSmarsEcTS _2NVQcOnbtdGIu9O-mB9-YE"
    loading_button_locator = (By.CSS_SELECTOR, "button[type='submit'][class*='_2NVQcOnbtdGIu9O-mB9-YE']")

    # появление второго класса (спиннера)
    wait.until(EC.presence_of_element_located(loading_button_locator))

    # второй класс исчезает и исчезает спиннер
    wait.until(EC.invisibility_of_element_located(loading_button_locator))

    error_locator = (By.XPATH, "//div[contains(@class, '_1W_6HXiG4JJ0By1qN_0fGZ')]")
    error_message = wait.until(EC.visibility_of_element_located(error_locator))

    assert "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова." in error_message.text
