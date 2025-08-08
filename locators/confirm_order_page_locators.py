from selenium.webdriver.common.by import By

class PageConfirmLocators:
    ORDER_CONFIRMED_MESSAGE = (By.XPATH, "//div[contains(@class,'Order_ModalHeader')]")  # Локатор для сообщения об успешном создании заказа