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
        assert tensor_main_page.check_power_in_people()

    def test_step_2(self, driver):
        expected_result = 'https://tensor.ru/about'
        tensor_main_page = TensorMainPage(driver)
        tensor_main_page.click_power_in_people_read_more()
        result = tensor_main_page.get_current_url()
        assert expected_result == result

    def test_step_3(self, driver):
        tensor_about_page = TensorAboutPage(driver)
        img_size_list = tensor_about_page.get_working_img_sizes()
        assert all(
            img_size_list[0]['width'] == img['width'] and img_size_list[0]['height'] == img['height']
            for img in img_size_list[1:]
        )


class TestSuit2:
    pass