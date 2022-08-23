from pages.base_page import BasePage


class LoginPage(BasePage):
    scouts_panel_xpath = "//h5"
    login_field_xpath = " , //child::div/input"
    password_field_xpath = "//*[@name='password'] "
    remind_password_xpath = "//*[text()=’Remind password’]"
    language_dropdown_en_xpath = "//input[@value='en'] ,"
    language_dropdown_pl_xpath = "[value=pl]"
    sign_in_button_xpath = "//*[@type='submit']"
    email = "user01@getnada.com"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
