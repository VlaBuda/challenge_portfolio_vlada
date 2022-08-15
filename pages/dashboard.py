from pages.base_page import BasePage


class Dashboard(BasePage):
    scouts_panel_xpath = "//child::div/h5, //h5"

    login_field_xpath = "//input[@id='login'] , //*[@name='login']  , //child::div/input"

    password_field_xpath = "[name=password] , //*[@name='password']  , //input[@id=’password’] "

    remind_password_xpath = "//*[text()=’Remind password’] , //a , //child::div/a"

    language_dropdown_en_xpath = "//input[@value='en'] , [value=en] , //input[@class='MuiSelect-nativeInput']"

    language_dropdown_pl_xpath = "[value=pl] , //input[@value='pl'] , //input[@class=’MuiSelect-nativeInput’]"

    sign_in_button_xpath = "//*[@type='submit'] , //child::div/button"
