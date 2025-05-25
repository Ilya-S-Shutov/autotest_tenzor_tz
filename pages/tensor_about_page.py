from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from utils.logs import log_selenium_actions
from .base_page import BasePage


class TensorAboutPage(BasePage):
    WORKING_IMGS_LOCATOR = (By.CSS_SELECTOR, 'div.tensor_ru-About__block3 img')

    def __init__(self, driver: WebDriver, static_url: str = 'https://tensor.ru/about'):
        super().__init__(driver, static_url)

    @log_selenium_actions
    def get_working_img_sizes(self) -> list[dict[str, int]]:
        """Получить размеры изображений из блока "Работаем"."""
        imgs_list = self.find_elements(self.WORKING_IMGS_LOCATOR)
        return [img.size for img in imgs_list]




