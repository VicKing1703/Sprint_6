# import pytest
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.firefox.options import Options
# from webdriver_manager.firefox import GeckoDriverManager
# from data import Data
#
#
# @pytest.fixture
# def driver():
#     service = Service(executable_path='C:/WebDriver/bin/geckodriver')  #GeckoDriverManager().install())
#     options = Options()
#     options.add_argument(Data.WIDTH)
#     options.add_argument(Data.HEIGHT)
#     driver = webdriver.Firefox(service=service, options=options)
#     driver.get(Data.URL_SCOOTER)
#     yield driver
#     driver.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from data import Data


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(Data.URL_SCOOTER)
    yield driver
    driver.quit()
