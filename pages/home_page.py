import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators.home_page_locators import HomePageLocators 
from selenium.webdriver.support import expected_conditions as EC
from src.data import DataInfo


# Домашняя страница
class HomePage(BasePage):

    @allure.step('Открываем браузер')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Клик на вопрос из списка в блоке "Вопросы о важном"')
    def click_faq_question(self, index):  # Нажатие на вопрос в блоке "Вопросы о важном"
        self.click(HomePageLocators.QUESTIONS_LOCATORS[index])

    @allure.step('Получение текста ответа на вопрос, который кликнули курсором')
    def get_faq_answer_text(self, index):  # Получение текста ответа на вопрос
        return self.get_text(HomePageLocators.ANSWERS_LOCATORS[index])

    @allure.step('Нажатие кнопки "Заказать"')
    def click_order_button(self, button_type="top"):  # Нажатие кнопки "Заказать"
        if button_type == "top":
            self.click(HomePageLocators.ORDER_BUTTON_SMALL_TOP)
        else:
            self.click(HomePageLocators.COOKIES_BUTTON)
            self.click(HomePageLocators.ORDER_BUTTON_BIG_MIDDLE)

    @allure.step('Нажатие на логотип "Самокат"')
    def click_samokat_logo(self):  # Нажатие на лого Самокат
        self.click(HomePageLocators.SAMOKAT_LOGO)

    @allure.step('Нажатие на логотип Яндекс')
    def click_yandex_logo(self):  # Нажатие на лого Яндекс
        self.click(HomePageLocators.YANDEX_LOGO)

    @allure.step('Ожидание загрузки и переключение на новую вкладку')
    def yandex_logo_wait_switch(self):
        self.WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))  # Переключиться на новую вкладку
        self.driver.switch_to.window(self.driver.window_handles[1])  # Явное ожидание загрузки страницы
        self.WebDriverWait(self.driver, 10).until(EC.url_to_be(DataInfo.url_dzen))    
