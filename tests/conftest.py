import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


BASE_URL = "https://b2c.passport.rt.ru/"

@pytest.fixture
def driver():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    options = Options()
    # добавляем параметр отключающий скрывающи вход через оболочку
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.get(BASE_URL)
    driver.implicitly_wait(10)

    yield driver

    driver.quit()