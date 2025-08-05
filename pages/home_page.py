from selenium.webdriver.common.by import By
from .base_page import BasePage


# Домашняя страница
class HomePage(BasePage):
    # Локаторы для блока "Вопросы о важном"
    QUESTIONS_LOCATORS = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7"),
    ]

    ANSWERS_LOCATORS = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"),
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7"),
    ]

    # Локаторы для кнопок "Заказать"
    ORDER_BUTTON_SMALL_TOP = (
        By.XPATH,
        "//div[contains(@class,'Header_Nav')]/button[contains(@class, 'Button_Button')]",
    )
    ORDER_BUTTON_BIG_MIDDLE = (
        By.XPATH,
        "//div[contains(@class,'Home_FinishButton')]/button[contains(@class, 'Button_Button')]",
    )

    # Локаторы для логотипов
    SAMOKAT_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")

    # Локатор для закрытия сообщения о куках
    COOKIES_BUTTON = (By.ID, "rcc-confirm-button")

    def __init__(self, driver):
        self.driver = driver

    def click_faq_question(self, index):  # Нажатие на вопрос в блоке "Вопросы о важном"
        self.click(self.QUESTIONS_LOCATORS[index])

    def get_faq_answer_text(self, index):  # Получение текста ответа на вопрос
        return self.get_text(self.ANSWERS_LOCATORS[index])

    def click_order_button(self, button_type="top"):  # Нажатие кнопки "Заказать"
        if button_type == "top":
            self.click(self.ORDER_BUTTON_SMALL_TOP)
        else:
            self.click(self.COOKIES_BUTTON)
            self.click(self.ORDER_BUTTON_BIG_MIDDLE)

    def click_samokat_logo(self):  # Нажатие на лого Самокат
        self.click(self.SAMOKAT_LOGO)

    def click_yandex_logo(self):  # Нажатие на лого Яндекс
        self.click(self.YANDEX_LOGO)
