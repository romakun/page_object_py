from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.common.by import By


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_path = None
    accept_cookie_btn_loc = (By.CSS_SELECTOR, 'button.fc-cta-consent')

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        self.driver.get(f'{self.base_url}{self.page_path}')
        #self.driver.find_element(*self.accept_cookie_btn_loc).click()

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def scroll_to(self, element: WebElement):
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    def click(self, element: WebElement):
        self.scroll_to(element)
        element.click()

    def type(self, element: WebElement, text):
        self.scroll_to(element)
        element.send_keys(text)
