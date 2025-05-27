import logging
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--update_driver', action='store', default='n',
                     help="Update webdriver version (y/n).")


@pytest.fixture(scope='class')
def driver(request):
    if request.config.getoption('--update_driver') == 'y':
        ChromeDriverManager.install()

    chrome_options = Options()
    prefs = {
        "download.default_directory": os.path.join(os.getcwd(), 'tests'),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }

    chrome_options.add_experimental_option("prefs", prefs)
    my_driver = webdriver.Chrome(options=chrome_options)
    my_driver.maximize_window()
    yield my_driver
    my_driver.quit()


@pytest.fixture(scope='session', autouse=True)
def configure_logging():
    logger = logging.getLogger('myLogger')
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    yield

    logger.removeHandler(handler)