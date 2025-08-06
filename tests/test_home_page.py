import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from pages.home_page import HomePage
from selenium.webdriver.support import expected_conditions as EC
from src.data import DataInfo


class TestHomePage:
    @allure.title('Проверка перехода при нажатии на логотип «Самокат» на домашнюю страницу сервиса')
    @allure.description('Убедимся в том, что при нажатии на логотип "Самокат" будет переход на домашнюю страницу')
    
    def test_click_samokat_logo(self, firefox_driver):  # Проверить, что при нажатии на лого «Самоката» происходит переход на домашнюю страницу сервиса
        self.home_page = HomePage(firefox_driver)
        self.home_page.click_samokat_logo()
        assert firefox_driver.current_url == DataInfo.url, ("Не произошел переход на домашнюю страницу")

    @allure.title("Проверка перехода при нажатии на логотип Яндекс на страницу Дзен.ру")
    @allure.description("Убедимся в том, что при нажатии на логотип Яндекс будет переход на страницу Дзен.ру")

    def test_click_yandex_logo(self, firefox_driver):  # Проверить, что при нажатии на лого Яндекс в новом окне откроется страница Дзен.ру
        self.home_page = HomePage(firefox_driver)
        self.home_page.click_yandex_logo()
        self.home_page.yandex_logo_wait_switch() 
        assert DataInfo.url_dzen == firefox_driver.current_url, ("Не произошел переход на страницу Дзен")