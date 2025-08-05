from selenium.webdriver.common.by import By
from .base_page import BasePage



class ConfirmOrderPage(BasePage):  # Страница подтверждения заказа
    # Локатор для сообщения об успешном создании заказа
    ORDER_CONFIRMED_MESSAGE = (By.XPATH, "//div[contains(@class,'Order_ModalHeader')]")

    def __init__(self, driver):
        self.driver = driver

    def get_order_confirmed_message(self):  # Сообщение об успешно созданном заказе
        return self.get_text(self.ORDER_CONFIRMED_MESSAGE)

    def is_order_confirmed(self):  # Проверка наличия сообщения об успешно созданном заказе
        return self.is_displayed(self.ORDER_CONFIRMED_MESSAGE)