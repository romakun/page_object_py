import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.sale_page import SalePage
from pages.registration_page import RegistrationPage
from pages.eco_friendly_page import EcoFriendlyPage


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('window-size=1920,1080')
    options.add_argument('--headless')
    options.add_argument('--disable-web-security')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(5)
    return chrome_driver


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def registration_page(driver):
    return RegistrationPage(driver)


@pytest.fixture()
def eco_friendly_page(driver):
    return EcoFriendlyPage(driver)
