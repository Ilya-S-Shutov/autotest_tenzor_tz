import os
import re

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from utils.logs import log_selenium_actions
from .base_page import BasePage


class SabyDownloadPage(BasePage):
    DOWNLOAD_LINK_LOCATOR = (By.PARTIAL_LINK_TEXT, 'Скачать (Exe') # "//a[starts-with(text(), 'Скачать (Exe ')]"

    def __init__(self, driver: WebDriver, static_url: str = 'https://saby.ru/download'):
        super().__init__(driver, static_url)

    @log_selenium_actions
    def click_download_link(self) -> tuple[str, float]:
        """Нажать на ссылку скачивания веб-установщика для windows."""
        file_size = re.search(r'\d{1,4}\.\d{2}', self.find_element(self.DOWNLOAD_LINK_LOCATOR).text).group()
        file_name = os.path.basename(self.find_element(self.DOWNLOAD_LINK_LOCATOR).get_attribute('href'))
        file_path = os.path.join(os.getcwd(), 'tests', file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
        self.click(self.DOWNLOAD_LINK_LOCATOR)
        return file_path, float(file_size)

