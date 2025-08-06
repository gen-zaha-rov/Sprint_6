import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators.confirm_order_page_locators import PageConfirmLocators  


class ConfirmOrderPage(BasePage):  # Страница подтверждения заказа

    @allure.step('Открываем браузер')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Получаем сообщение об успешно созданном заказе')
    def get_order_confirmed_message(self):  # Сообщение об успешно созданном заказе
        return self.get_text(PageConfirmLocators.ORDER_CONFIRMED_MESSAGE)

    @allure.step('Проверка на наличие сообщения об успешно созданном заказе')
    def is_order_confirmed(self):  # Проверка наличия сообщения об успешно созданном заказе
        return self.is_displayed(PageConfirmLocators.ORDER_CONFIRMED_MESSAGE)