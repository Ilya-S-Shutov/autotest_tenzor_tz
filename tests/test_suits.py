import pytest

from pages.saby_contacts_page import SabyContactsPage
from pages.saby_main_page import SabyMainPage
from pages.tensor_about_page import TensorAboutPage
from pages.tensor_main_page import TensorMainPage


class TestSuit1:

    def test_step_1(self, driver):
        saby_main_page = SabyMainPage(driver)
        saby_main_page.open()
        saby_main_page.go_to_contacts()

        saby_contacts_page = SabyContactsPage(driver)
        saby_contacts_page.click_clients_banner()

        tensor_main_page = TensorMainPage(driver)
        assert tensor_main_page.check_power_in_people(), 'Отсутствует блок "Сила в людях"'

    def test_step_2(self, driver):
        expected_result = 'https://tensor.ru/about'
        tensor_main_page = TensorMainPage(driver)
        tensor_main_page.click_power_in_people_read_more()
        result = tensor_main_page.get_current_url()
        assert expected_result == result, f'Текущий url: {result} не соответствует ожидаемому: {expected_result}'

    def test_step_3(self, driver):
        tensor_about_page = TensorAboutPage(driver)
        img_size_list = tensor_about_page.get_working_img_sizes()
        assert all(
            img_size_list[0]['width'] == img['width']
            and
            img_size_list[0]['height'] == img['height']
            for img in img_size_list[1:]
        ), 'Размеры картинок не совпадают'


class TestSuit2:
    def test_step_1(self, driver):
        expected_region_name = 'Свердловская обл.'
        saby_main_page = SabyMainPage(driver)
        saby_main_page.open()
        saby_main_page.go_to_contacts()
        saby_contacts_page = SabyContactsPage(driver)
        region_info = saby_contacts_page.get_current_region_info()
        assert expected_region_name == region_info['region_name'], \
            f'Выбран регион: {region_info['region_name']}, ожидался: {expected_region_name}.'
        assert region_info['partners'], 'Отсутствует список партнёров.'

    def test_step_2(self, driver):
        expected_region_info = {
            'url_part': '41-kamchatskij-kraj',
            'region_name': 'Камчатский край'
        }
        saby_contacts_page = SabyContactsPage(driver)
        start_partners_dict = saby_contacts_page.get_partners_list()
        saby_contacts_page.change_region('41 Камчатский край')
        result_region_info = saby_contacts_page.get_current_region_info()

        assert expected_region_info['url_part'] in result_region_info['url'], \
            (f'Url: {result_region_info['url']} не содержит ожидаемой части:'
             f' "{expected_region_info['url_part']}".')

        assert expected_region_info['region_name'] == result_region_info['region_name'], \
        (f'Ожидаемое имя региона: "{expected_region_info['region_name']}", '
         f'получено: "{result_region_info['region_name']}".')

        assert start_partners_dict != result_region_info['partners'], 'Список партнёров не изменился.'
