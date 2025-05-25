from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from utils.logs import log_selenium_actions
from .base_page import BasePage


class SabyMainPage(BasePage):
    CONTACTS_LOCATOR = (By.CSS_SELECTOR, "div.js-ContactsMenu")
    OFFICES_LOCATOR = (By.PARTIAL_LINK_TEXT, "офисов в регионе")

    def __init__(self, driver: WebDriver, static_url: str = 'https://saby.ru'):
        super().__init__(driver, static_url)

    @log_selenium_actions
    def go_to_contacts(self) -> None:
        self.click(self.CONTACTS_LOCATOR)
        self.click(self.OFFICES_LOCATOR)

