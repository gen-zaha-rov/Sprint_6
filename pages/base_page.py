import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from src.data import DataInfo


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
        
    @allure.step('Проверка соответствия текущей странице ожидаемой')
    def is_current_url_correct(self, expected_url):
        return self.driver.current_url == expected_url  

    @allure.step('Ожидание загрузки и переключение на новую вкладку')
    def yandex_logo_wait_switch(self):
        self.WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))  # Переключиться на новую вкладку
        self.driver.switch_to.window(self.driver.window_handles[1])  # Явное ожидание загрузки страницы
        self.WebDriverWait(self.driver, 10).until(EC.url_to_be(DataInfo.url_dzen))      
