from pages.main_page import MainPage
from locators import RegLocators
from selenium.webdriver.common.keys import Keys


class RegPage(MainPage):

    def registration_click_button(self):
        reg_btn = self.driver.find_element(*RegLocators.reg_btn)
        reg_btn.click()

    def name_input_data(self, nameu):
        name = self.driver.find_element(*RegLocators.first_name)
        name.send_keys(nameu)

    def last_user_name_input_data(self, last):
        last_user_name = self.driver.find_element(*RegLocators.last_name)
        last_user_name.send_keys(last)

    def user_mail_input(self, reg_mail):
        user_mail = self.driver.find_element(*RegLocators.regi_mail)
        user_mail.send_keys(reg_mail)

    def password_input_data(self, reg_pwd):
        user_passw = self.driver.find_element(*RegLocators.regi_pwd)
        user_passw.send_keys(reg_pwd)

    def password_confirm_input_data(self, reg_pwd_rep):
        user_confpwd = self.driver.find_element(*RegLocators.regi_repassw)
        user_confpwd.send_keys(reg_pwd_rep)

    def select_region(self, region_name):
        choice_reg = self.driver.find_element(*RegLocators.region)
        choice_reg.click()
        choice_reg.send_keys(Keys.BACKSPACE * 8)
        choice_reg.send_keys(region_name)

    def submit_button_click(self):
        submit = self.driver.find_element(*RegLocators.subm_btn)
        submit.click()

    def registr_user(self, nameu: str,
                     last: str,
                     region_name: str,
                     reg_mail: str,
                     reg_pwd: str,
                     reg_pwd_rep: str) -> None:
        self.registration_click_button()
        self.name_input_data(nameu)
        self.last_user_name_input_data(last)
        self.user_mail_input(reg_mail)
        self.password_input_data(reg_pwd)
        self.password_confirm_input_data(reg_pwd_rep)
        self.select_region(region_name)
        self.submit_button_click()
