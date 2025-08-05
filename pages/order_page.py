from selenium.webdriver.common.by import By
from .base_page import BasePage


class OrderPage(BasePage):  # Страница для оформления заказа ("Для кого самокат")
    # Локаторы для полей формы
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    DELIVERY_ADDRESS = (
        By.XPATH,
        "//input[@placeholder='* Адрес: куда привезти заказ']",
    )
    METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DELIVERY_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-arrow")
    COLOR_CHECKBOX = (By.XPATH, "//input[@type='checkbox']")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'Order_Buttons')]/button[contains(text(), 'Заказать')]",
    )
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")

    def __init__(self, driver):
        self.driver = driver

    def fill_personal_data(
        self, first_name, last_name, delivery_address, metro_station, phone
    ):  # Заполнить форму заказа, часть 1 из 2
        self.send_keys(self.FIRST_NAME, first_name)
        self.send_keys(self.LAST_NAME, last_name)
        self.send_keys(self.DELIVERY_ADDRESS, delivery_address)
        self.click(self.METRO_STATION)
        metro_station_locator = (
            By.XPATH,
            f".//div[@class='select-search__select']//button[contains(., '{metro_station}')]",
        )
        self.click(metro_station_locator)
        self.send_keys(self.PHONE, phone)
        self.click(self.NEXT_BUTTON)

    def fill_rental_data(
        self, delivery_date, rental_period, color, comment
    ):  # Заполнить форму заказа, часть 2 из 2
        self.send_keys(self.DELIVERY_DATE, delivery_date)
        self.click(self.RENTAL_PERIOD_DROPDOWN)
        rental_period_locator = (By.XPATH, f"//div[text()='{rental_period}']")
        self.click(rental_period_locator)
        color_locator = (By.XPATH, f".//label[text()='{color}']")
        self.click(color_locator)
        self.send_keys(self.COMMENT, comment)
        self.click(self.ORDER_BUTTON)

    def confirm_order(self):  # Подтвердить заказ
        self.click(self.CONFIRM_ORDER_BUTTON)
