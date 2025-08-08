from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Локаторы для полей формы
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    DELIVERY_ADDRESS = (
        By.XPATH,
        "//input[@placeholder='* Адрес: куда привезти заказ']",
    )
    METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    metro_station_locator = (By.XPATH,f".//div[@class='select-search__select']//button[contains(., '{METRO_STATION}')]",)
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DELIVERY_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    rental_period_locator = (By.XPATH, f"//div[text()='{rental_period}']")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-arrow")
    COLOR_CHECKBOX = (By.XPATH, "//input[@type='checkbox']")
    color_locator = (By.XPATH, f".//label[text()='{color}']")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'Order_Buttons')]/button[contains(text(), 'Заказать')]",
    )
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")