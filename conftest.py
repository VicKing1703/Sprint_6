import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from data import Data


@pytest.fixture
def driver():
    service = Service(GeckoDriverManager().install())
    options = Options()
    options.add_argument(Data.WINDIW_SIZE)
    driver = webdriver.Firefox(service=service, options=options)
    driver.get(Data.BACE_URL)
    yield driver
    driver.quit()
