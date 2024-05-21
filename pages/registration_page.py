from pages.base_page import BasePage
from pages.locators import registration_locators as loc
from pages.errors import registration_errors as err
import allure


class RegistrationPage(BasePage):
    page_path = '/customer/account/create/'

    @allure.step('click_submit_btn')
    def click_submit_btn(self):
        submit_btn = self.find(loc.submit_btn_loc)
        self.click(submit_btn)

    @allure.step('check_required_fields')
    def check_required_fields(self):
        self.click_submit_btn()

        first_name_err = self.find(loc.first_name_err_loc)
        last_name_err = self.find(loc.last_name_err_loc)
        email_err = self.find(loc.email_err_loc)
        password_err = self.find(loc.password_err_loc)
        confirm_password_err = self.find(loc.password_err_confirmation_loc)

        assert first_name_err.text == err.required_field_error
        assert last_name_err.text == err.required_field_error
        assert email_err.text == err.required_field_error
        assert password_err.text == err.required_field_error
        assert confirm_password_err.text == err.required_field_error

    @allure.step('check_email_format_error')
    def check_email_format_error(self, text):
        email_field = self.find(loc.email_loc)
        self.type(email_field, text)
        self.click_submit_btn()
        email_err = self.find(loc.email_err_loc)

        assert email_err.text == err.email_format_error

    @allure.step('check_password_errors')
    def check_password_errors(self, text, error):
        password_field = self.find(loc.password_loc)
        self.type(password_field, text)
        self.click_submit_btn()
        password_err = self.find(loc.password_err_loc)

        assert password_err.text == error
