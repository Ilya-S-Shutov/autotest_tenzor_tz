# from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from utils.logs import log_selenium_actions


class BasePage:

    def __init__(self, driver: WebDriver, url: str):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.URL = url

    @log_selenium_actions
    def open(self) -> None:
        """Открыть страницу."""
        self.driver.get(self.URL)

    @log_selenium_actions
    def find_element(self, locator: tuple[str, str]) -> WebElement | str:
        """Вернуть первый найденный по локатору элемент."""
        return self.wait.until(EC.presence_of_element_located(locator),
                                   message=f"Can't find element by locator {locator}.")

    @log_selenium_actions
    def find_elements(self, locator: tuple[str, str]) -> list[WebElement] | str:
        return self.wait.until(EC.presence_of_all_elements_located(locator),
                               message=f"Can't find elements by locator {locator}.")

    @log_selenium_actions
    def click(self, locator: tuple[str, str]) -> None:
        """Кликнуть на первый найденный по локатору элемент."""
        self.wait.until(EC.element_to_be_clickable(locator),
                                message=f"Can't find element by locator {locator}.").click()

    # @log_selenium_actions
    # def add_cookie(self, name: str, value: str, **cookie_options) -> None:
    #     cookie_options['name'] = name
    #     cookie_options['value'] = value
    #     self.driver.add_cookie(cookie_options)
    #     self.refresh()
    #
    # @log_selenium_actions
    # def refresh(self) -> None:
    #     self.driver.refresh()

    @log_selenium_actions
    def get_current_url(self) -> str:
        """Получить url текущей страницы."""
        return self.driver.current_url

    @log_selenium_actions
    def switch_to_new_tab(self) -> None:
        """Переключиться на новую вкладку."""
        self.wait.until(lambda dr: len(dr.window_handles) > 1)
        new_tab = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_tab)
