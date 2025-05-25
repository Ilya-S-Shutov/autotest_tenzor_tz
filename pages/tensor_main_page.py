from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from utils.logs import log_selenium_actions
from .base_page import BasePage


class TensorMainPage(BasePage):
    POWER_IN_PEOPLE_LOCATOR = (By.XPATH, '//div[contains(@class, "block")]/p[normalize-space()="Сила в людях"]')
    POWER_IN_PEOPLE_READ_MORE_LOCATOR = (By.XPATH, '//a[@href="/about" and text()="Подробнее"]')

    def __init__(self, driver: WebDriver, static_url: str = 'https://tensor.ru/'):
        super().__init__(driver, static_url)

    @log_selenium_actions
    def check_power_in_people(self) -> bool:
        """Проверить наличие блока "Сила в людях"."""
        if self.find_element(self.POWER_IN_PEOPLE_LOCATOR):
            return True

    @log_selenium_actions
    def click_power_in_people_read_more(self) -> None:
        """Кликнуть на ссылку "Подробнее" в блоке "Сила в людях"."""
        self.click(self.POWER_IN_PEOPLE_READ_MORE_LOCATOR)


