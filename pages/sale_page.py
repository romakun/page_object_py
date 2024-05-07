from pages.base_page import BasePage
from pages.locators import sale_locators as loc


class SalePage(BasePage):
    page_path = '/sale.html'

    def check_header(self):
        header = 'Sale'
        page_header = self.find(loc.page_title_loc)
        assert page_header.text == header

    def check_sidebar_section_titles(self):
        section_titles = ["WOMEN'S DEALS", "MENS'S DEALS", 'GEAR DEALS']
        sidebar_section_titles_elements = self.find_all(loc.sidebar_section_titles_loc)
        sidebar_section_titles = [element.text for element in sidebar_section_titles_elements]
        assert sidebar_section_titles == section_titles

    def check_menu_tab_is_active(self):
        sale_menu_tab = self.find(loc.sale_menu_tab_loc)
        assert sale_menu_tab.get_attribute('class').__contains__('active')
