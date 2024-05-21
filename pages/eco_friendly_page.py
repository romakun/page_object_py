from pages.base_page import BasePage
from pages.locators import eco_friendly_locators as loc
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class EcoFriendlyPage(BasePage):
    page_path = '/collections/eco-friendly.html'

    @allure.step('check_product_names')
    def check_product_names(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.banner_span_loc))
        product_names = self.get_product_names()
        assert all(item for item in product_names)

    @allure.step('get_product_names')
    def get_product_names(self):
        product_names_elements = self.find_all(loc.product_names_loc)
        return [element.text for element in product_names_elements]

    @allure.step('get_product_prices')
    def get_product_prices(self):
        product_prices = self.find_all(loc.product_prices_loc)
        return [float(element.text.replace('$', '')) for element in product_prices]

    @allure.step('change_product_grid_mode')
    def change_product_grid_mode(self, grid_mode):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.banner_span_loc))
        grid_mode_btn = self.find(loc.grid_btn_loc)
        list_mode_btn = self.find(loc.list_btn_loc)

        if grid_mode_btn.get_attribute('class').__contains__('active') and grid_mode == 'list':
            self.click(list_mode_btn)
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.banner_span_loc))
        elif list_mode_btn.get_attribute('class').__contains__('active') and grid_mode == 'grid':
            self.click(grid_mode_btn)
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.banner_span_loc))

    @allure.step('change_sorting_type')
    def change_sorting_type(self, value):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.banner_span_loc))
        sort_select = self.find(loc.sort_select_loc)
        sort_dropdown = Select(sort_select)
        sort_dropdown.select_by_value(value)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.banner_span_loc))

    @allure.step('change_sorting_order')
    def change_sorting_order(self, sort_order):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.banner_span_loc))
        sort_action = self.find(loc.sorter_action_loc)

        if sort_action.get_attribute('data-value') != sort_order:
            self.click(sort_action)
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.banner_span_loc))

    @allure.step('check_sort_by_name')
    def check_sort_by_name(self, sort_order):
        product_names = self.get_product_names()
        assert product_names == sorted(product_names, reverse=True if sort_order == 'asc' else False)

    @allure.step('check_sort_by_price')
    def check_sort_by_price(self, sort_order):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.banner_span_loc))
        product_prices_nums = self.get_product_prices()

        assert product_prices_nums == sorted(
            product_prices_nums,
            reverse=True if sort_order == 'asc' else False,
            key=float)

    @allure.step('sort_products')
    def sort_products(self, sort_type, sort_order):
        self.change_sorting_type(sort_type)
        self.change_sorting_order(sort_order)
