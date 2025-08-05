import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from data import Data


@pytest.fixture(scope="function")
def driver():
    # Cоздать и закрыть по завершении экземпляр Firefox
    firefox_options = FirefoxOptions()

    driver = webdriver.Firefox(options=firefox_options)
    driver.maximize_window()
    driver.get(Data.url)
    yield driver
    driver.quit()
