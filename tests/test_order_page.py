import allure
import pytest
from pages.home_page import HomePage
from pages.order_page import OrderPage
from pages.confirm_order_page import ConfirmOrderPage
from src.data import DataInfo


class TestOrder:
    @pytest.mark.parametrize("button_type", DataInfo.ORDER_BUTTON_TYPES)
    @pytest.mark.parametrize("first_name, last_name, delivery_address, metro_station, phone, delivery_date, rental_period, color, comment", DataInfo.ORDER_TEST_DATA)
        
    @allure.title('Проверка успешности создания заказа каждой из двух кнопок "Заказать"')
    @allure.description('Убедимся в том, после нажатия кнопки "Заказать" (хоть через верхнюю, хоть через нижнюю) открываются поля заказа, после заполнения валидными данными формируется заказ')

    def test_order_scooter(self, firefox_driver, button_type, first_name, last_name, delivery_address, metro_station, phone, delivery_date, rental_period, color, comment):  # Проверка на успешное создание заказа
        home_page = HomePage(firefox_driver)
        order_page = OrderPage(firefox_driver)
        confirm_order_page = ConfirmOrderPage(firefox_driver)
        home_page.click_order_button(button_type)
        order_page.fill_personal_data(first_name, last_name, delivery_address, metro_station, phone)
        order_page.fill_rental_data(delivery_date, rental_period, color, comment)
        order_page.confirm_order()
        assert confirm_order_page.is_order_confirmed(), ("Сообщение об успешном формировании заказа не вывелось на экран")
