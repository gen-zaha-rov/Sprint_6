import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage


class BasePage:
    @allure.step('Открываем браузер')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажатие на элемент, когда он стал кликабельным')
    def click(self, locator, timeout=8):  # Нажать на элемент
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()

    @allure.step('Получение текстового значения из элемента')
    def get_text(self, locator, timeout=8):  # Получить текстовое значение из элемента
        return (WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).text)

    @allure.step('Ввод значения в тестовом поле')
    def send_keys(self, locator, text, timeout=8):  # Ввод значения в тестовое поле
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).send_keys(text)

    @allure.step('Прокрутка страницы вниз до крайнего положения')
    def scroll_down_to_bottom(self): 
        self.home_page = HomePage()
        self.home_page.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Прокрутить в самый низ страницы   

    @allure.step('Проверка отображения элемента')
    def is_displayed(self, locator, timeout=8):  # Проверить отображение элемента
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
