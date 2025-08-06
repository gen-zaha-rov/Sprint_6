from selenium.webdriver.common.by import By


class HomePageLocators:
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