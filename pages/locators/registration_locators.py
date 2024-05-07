from selenium.webdriver.common.by import By

page_title_loc = (By.TAG_NAME, 'h1')
first_name_loc = (By.ID, 'firstname')
last_name_loc = (By.ID, 'lastname')
email_loc = (By.ID, 'email_address')
password_loc = (By.ID, 'password')
password_confirmation_loc = (By.ID, 'password-confirmation')
submit_btn_loc = (By.CSS_SELECTOR, 'button.submit')
first_name_err_loc = (By.ID, 'firstname-error')
last_name_err_loc = (By.ID, 'lastname-error')
email_err_loc = (By.ID, 'email_address-error')
password_err_loc = (By.ID, 'password-error')
password_err_confirmation_loc = (By.ID, 'password-confirmation-error')
