import allure
import pytest
from pages.home_page import HomePage
from pages.base_page import BasePage
from src.data import DataInfo


class TestHomePage(BasePage):
    @allure.title('Проверка перехода при нажатии на логотип «Самокат» на домашнюю страницу сервиса')
    @allure.description('Убедимся в том, что при нажатии на логотип "Самокат" будет переход на домашнюю страницу')
    
    def test_click_samokat_logo(self, firefox_driver):  # Проверить, что при нажатии на лого «Самоката» происходит переход на домашнюю страницу сервиса
        home_page = HomePage(firefox_driver)
        home_page.click_samokat_logo()
        assert home_page.is_current_url_correct(DataInfo.url), ("Не произошел переход на домашнюю страницу")

    @allure.title("Проверка перехода при нажатии на логотип Яндекс на страницу Дзен.ру")
    @allure.description("Убедимся в том, что при нажатии на логотип Яндекс будет переход на страницу Дзен.ру")

    def test_click_yandex_logo(self, firefox_driver):  # Проверить, что при нажатии на лого Яндекс в новом окне откроется страница Дзен.ру
        home_page = HomePage(firefox_driver)
        home_page.click_yandex_logo()
        home_page.yandex_logo_wait_switch() 
        assert home_page.is_current_url_correct(DataInfo.url_dzen), ("Не произошел переход на страницу Дзен")

        