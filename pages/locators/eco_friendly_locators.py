from selenium.webdriver.common.by import By


products_loc = (By.CLASS_NAME, 'product-item')
product_prices_loc = (By.XPATH, '//span[contains(@id, "product-price")]')
product_names_loc = (By.CLASS_NAME, 'product-item-name')
sort_select_loc = (By.ID, 'sorter')
sorter_action_loc = (By.CLASS_NAME, 'sorter-action')
grid_btn_loc = (By.CLASS_NAME, 'mode-grid')
list_btn_loc = (By.CLASS_NAME, 'mode-list')
banner_span_loc = (By.XPATH, '//span[@class="not-logged-in"]')
