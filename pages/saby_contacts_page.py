# import re

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from utils.logs import log_selenium_actions
from .base_page import BasePage


class SabyContactsPage(BasePage):
    TENSOR_CLIENTS_BANNER_LOCATOR = (By.CSS_SELECTOR, 'div#contacts_clients a[href = "https://tensor.ru/"] > img')

    def __init__(self, driver: WebDriver, static_url: str = 'https://saby.ru/contacts'):
        super().__init__(driver, static_url)
        # self.url_pattern = re.compile(rf'https://{static_url}/\d{2}')

    @log_selenium_actions
    def click_clients_banner(self) -> None:
        self.click(self.TENSOR_CLIENTS_BANNER_LOCATOR)
        self.switch_to_new_tab()
