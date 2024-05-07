from selenium.webdriver.common.by import By


page_title_loc = (By.TAG_NAME, 'h1')
sidebar_loc = (By.CLASS_NAME, 'sidebar-main')
sidebar_section_titles_loc = (By.XPATH, '//div[contains(@class, "sidebar-main")]//strong')
sale_menu_tab_loc = (By.XPATH, '//a[@id="ui-id-8"]/..')
