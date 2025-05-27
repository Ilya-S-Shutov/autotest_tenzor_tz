from selenium.common import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

from utils.logs import log_selenium_actions
from .base_page import BasePage


class SabyContactsPage(BasePage):
    TENSOR_CLIENTS_BANNER_LOCATOR = (By.CSS_SELECTOR, 'div#contacts_clients a[href = "https://tensor.ru/"] > img')
    CURRENT_REGION_CHOOSER_LOCATOR = (By.CSS_SELECTOR, 'div.sbisru-Contacts span.sbis_ru-Region-Chooser__text')
    PARTNER_ITEMS_LOCATOR = (By.CSS_SELECTOR, 'div[data-qa="item"')
    PARTNER_NAME_LOCATOR = (By.CSS_SELECTOR, 'div.sbisru-Contacts-List__name')

    def __init__(self, driver: WebDriver, static_url: str = 'https://saby.ru/contacts'):
        super().__init__(driver, static_url)

    @log_selenium_actions
    def click_clients_banner(self) -> None:
        """Кликнуть по баннеру "Тензор" и переключить вкладку."""
        self.click(self.TENSOR_CLIENTS_BANNER_LOCATOR)
        self.switch_to_new_tab()

    @log_selenium_actions
    def get_selected_region(self) -> str:
        """Получить название текущего выбранного региона."""
        return self.find_element(self.CURRENT_REGION_CHOOSER_LOCATOR).text

    @log_selenium_actions
    def get_partners_list(self) -> dict[str, list[str]]:
        """Возвращает партнёров, указанных в выбранном регионе."""
        items = self.find_elements(self.PARTNER_ITEMS_LOCATOR)
        result = dict()
        for item in items:
            item_parent_key = item.get_attribute('item-parent-key')
            if item_parent_key is None:
                result[item.text] = list()
            else:
                parent = self.find_element((By.CSS_SELECTOR, f'div[item-key="{item_parent_key}"'))
                result[parent.text].append(item.find_element(*self.PARTNER_NAME_LOCATOR).text)
        return result

    @log_selenium_actions
    def get_current_region_info(self) -> dict[str, str | dict[str, str]]:
        """Возвращает информацию о текущем активном регионе.

        Пример:
        info_dict = {
            'url': 'https://current.url/',
            'region_name': 'My Region',
            'partners': {
                'City 1': ['Partner1', 'Partner2'],
                'City 2': ['Partner3', 'Partner4'],
            }
        }
        """
        region_info_dict = {
            'url': self.get_current_url(),
            'region_name': self.get_selected_region(),
            'partners': self.get_partners_list()
        }
        return region_info_dict

    @log_selenium_actions
    def change_region(self, regions_name: str) -> None:
        target_locator = (By.XPATH, f'//li//span[contains(text(), "{regions_name}")]')
        self.click(self.CURRENT_REGION_CHOOSER_LOCATOR)
        ActionChains(self.driver).move_to_element(
            self.find_element(target_locator)
        ).click(
            self.find_element(target_locator)
        ).perform()
        try:
            self.wait.until(EC.text_to_be_present_in_element(self.CURRENT_REGION_CHOOSER_LOCATOR, regions_name))
        except TimeoutException:
            pass
        # self.click((By.XPATH, f'//li//span[contains(text(), "{part_regions_name}")]'))
