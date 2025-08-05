import allure
import pytest
from pages.home_page import HomePage
from pages.order_page import OrderPage
from pages.confirm_order_page import ConfirmOrderPage


class TestOrder:
    @pytest.mark.parametrize("button_type", ["top", "middle"])
    @pytest.mark.parametrize(
        "first_name, last_name, delivery_address, metro_station, phone, delivery_date, rental_period, color, comment",
        [
            (
                "Джордж",
                "Харрисон",
                "Москва, ул. Кропоткина, 49",
                "Лубянка",
                "89673121569",
                "03.08.2025",
                "двое суток",
                "чёрный жемчуг",
                "Чур с исправным звонком и фарой",
            ),
            (
                "Ринго",
                "Стар",
                "Москва, пр. Гагарина, 4010",
                "Сокол",
                "89182482826",
                "04.08.2025",
                "семеро суток",
                "серая безысходность",
                "Вход со двора за шлагбаумом",
            ),
        ],
    )


    @allure.step('Открываем браузер, заполняем все поля заказа, проверяем, что заказ создался')
    @allure.title('Проверка успешности создания заказа каждой из двух кнопок "Заказать"')
    @allure.description('Убедимся в том, после нажатия кнопки "Заказать" (хоть через верхнюю, хоть через нижнюю) открываются поля заказа, после заполнения валидными данными формируется заказ')

    def test_order_scooter(self, driver, button_type, first_name, last_name, delivery_address, metro_station, phone, delivery_date, rental_period, color, comment):  # Проверка на успешное создание заказа
        self.home_page = HomePage(driver)
        self.order_page = OrderPage(driver)
        self.confirm_order_page = ConfirmOrderPage(driver)
        self.home_page.click_order_button(button_type)
        self.order_page.fill_personal_data(
            first_name, last_name, delivery_address, metro_station, phone
        )
        self.order_page.fill_rental_data(delivery_date, rental_period, color, comment)
        self.order_page.confirm_order()
        assert self.confirm_order_page.is_order_confirmed(), ("Сообщение об успешном формировании заказа не вывелось на экран")
