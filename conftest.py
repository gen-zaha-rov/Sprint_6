import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from src.data import DataInfo


@pytest.fixture(scope="function")
def firefox_driver():
    # Cоздать и закрыть по завершении экземпляр Firefox
    firefox_options = FirefoxOptions()

    driver = webdriver.Firefox(options=firefox_options)
    driver.maximize_window()
    driver.get(DataInfo.url)
    yield driver
    driver.quit()
