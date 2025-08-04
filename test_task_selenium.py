import pytest
from faker import Faker

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

STEAM_URL = "https://store.steampowered.com/"
WAIT_TIME = 15

# Чтобы убедиться, что страница загрузилась
STEAM_LOGO_LOCATOR = (By.XPATH, "//*[@id='global_header']//a[contains(@href, 'steampowered.com')]")

LOGIN_BUTTON_LOCATOR = (By.XPATH, "//a[contains(@class, 'global_action_link') and text()='войти']")

USERNAME_INPUT_LOCATOR = (
    By.XPATH, "//form//input[@type='text']")

PASSWORD_INPUT_LOCATOR = (
    By.XPATH, "//form//input[@type='password']")

SIGN_IN_BUTTON_LOCATOR = (By.XPATH, "//form//button[@type='submit']")

LOADING_SPINNER_LOCATOR = (By.XPATH, "//form//button[contains(@class, ' ') and @type='submit']")

ERROR_LOCATOR = (
    By.XPATH,
    "//form//button[@type='submit']/following::div[normalize-space()][1]"
)


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(STEAM_URL)
    yield driver
    driver.quit()


def test_steam(driver):
    fake = Faker()

    username_data = fake.user_name()

    password_data = fake.password(length=16, special_chars=True, upper_case=True, lower_case=True, digits=True)

    wait = WebDriverWait(driver, WAIT_TIME)

    # Убеждаемся в загрузке страницы.
    # wait.until(EC.visibility_of_element_located(STEAM_LOGO_LOCATOR))

    expected_url = STEAM_URL
    actual_url = driver.current_url

    assert expected_url == actual_url, \
        f"Открылась не главная страница.\n" \
        f"Ожидали URL: '{expected_url}'\n" \
        f"Фактический URL: '{actual_url}'"

    login_button = wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_LOCATOR))

    login_button.click()

    # Заполняем поля
    username = wait.until(EC.visibility_of_element_located(USERNAME_INPUT_LOCATOR))
    password = wait.until(EC.visibility_of_element_located(PASSWORD_INPUT_LOCATOR))

    username.send_keys(username_data)
    password.send_keys(password_data)

    sign_in_button = wait.until(EC.element_to_be_clickable(SIGN_IN_BUTTON_LOCATOR))

    sign_in_button.click()

    # Загрузка и исчезновение спиннера
    wait.until(EC.presence_of_element_located(LOADING_SPINNER_LOCATOR))
    wait.until(EC.invisibility_of_element_located(LOADING_SPINNER_LOCATOR))

    # Текст ошибки
    error_message = wait.until(EC.visibility_of_element_located(ERROR_LOCATOR))

    expected_error = "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова."
    actual_error = error_message.text.strip()

    assert expected_error in actual_error, \
        f"Текст ошибки не соответствует ожидаемому.\n" \
        f"Ожидаемый текст содержит: '{expected_error}'\n" \
        f"Фактический текст: '{actual_error}'"
