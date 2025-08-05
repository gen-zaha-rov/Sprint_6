from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator, timeout=8):  # Нажать на элемент
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def get_text(self, locator, timeout=8):  # Получить текстовое значение из элемента
        return (
            WebDriverWait(self.driver, timeout)
            .until(EC.visibility_of_element_located(locator))
            .text
        )

    def send_keys(self, locator, text, timeout=8):  # Ввод значения в тестовое поле
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def is_displayed(self, locator, timeout=8):  # Проверить отображение элемента
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False
