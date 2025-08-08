import allure
from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators 


class OrderPage(BasePage):  # Страница для оформления заказа ("Для кого самокат")

    @allure.step('Заполнение формы заказа, страница 1 из 2')
    def fill_personal_data(self, first_name, last_name, delivery_address, metro_station, phone):  # Заполнить форму заказа, часть 1 из 2
        self.send_keys(OrderPageLocators.FIRST_NAME, first_name)
        self.send_keys(OrderPageLocators.LAST_NAME, last_name)
        self.send_keys(OrderPageLocators.DELIVERY_ADDRESS, delivery_address)
        self.click(OrderPageLocators.METRO_STATION)
        self.click(OrderPageLocators.metro_station_locator)
        self.send_keys(OrderPageLocators.PHONE, phone)
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнение формы заказа, страница 2 из 2')
    def fill_rental_data(self, delivery_date, rental_period, color, comment):  # Заполнить форму заказа, часть 2 из 2
        self.send_keys(OrderPageLocators.DELIVERY_DATE, delivery_date)
        self.click(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)   
        self.click(OrderPageLocators.rental_period_locator, rental_period)
        self.click(OrderPageLocators.color_locator, color)
        self.send_keys(OrderPageLocators.COMMENT, comment)
        self.click(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Нажатие кнопки подтверждения заказа')
    def confirm_order(self):  # Подтвердить заказ
        self.click(OrderPageLocators.CONFIRM_ORDER_BUTTON)
