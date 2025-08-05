import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from pages.home_page import HomePage
from selenium.webdriver.support import expected_conditions as EC
from data import Data


class TestHomePage:
    @allure.step('Открываем браузер, нажимаем на логотип «Самокат» и ожидаем переход на домашнюю страницу сервиса')
    @allure.title('Проверка перехода при нажатии на логотип «Самокат» на домашнюю страницу сервиса')
    @allure.description('Убедимся в том, что при нажатии на логотип "Самокат" будет переход на домашнюю страницу')
    
    def test_click_samokat_logo(self, driver):  # Проверить, что при нажатии на лого «Самоката» происходит переход на домашнюю страницу сервиса
        self.main_page = HomePage(driver)
        self.main_page.click_samokat_logo()
        assert driver.current_url == Data.url, ("Не произошел переход на домашнюю страницу")

    @allure.step("Открываем браузер и нажимаем на логотип Яндекс и ожидаем переход на Дзен.ру")
    @allure.title("Проверка перехода при нажатии на логотип Яндекс на страницу Дзен.ру")
    @allure.description("Убедимся в том, что при нажатии на логотип Яндекс будет переход на страницу Дзен.ру")

    def test_click_yandex_logo(self, driver):  # Проверить, что при нажатии на лого Яндекс в новом окне откроется страница Дзен.ру
        self.main_page = HomePage(driver)
        self.main_page.click_yandex_logo()
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))  # Переключиться на новую вкладку
        driver.switch_to.window(driver.window_handles[1])  # Явное ожидание загрузки страницы
        WebDriverWait(driver, 10).until(EC.url_to_be(Data.url_dzen))
        assert Data.url_dzen == driver.current_url, ("Не произошел переход на страницу Дзен")