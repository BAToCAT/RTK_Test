from pages.main_page import MainPage
from locators import RegLocators
from selenium.webdriver.common.keys import Keys

class RegPage(MainPage):

    def registr_user(self, nameu: str,
                    last: str,
                    region_name: str,
                    reg_mail: str,
                    reg_pwd: str,
                    reg_pwd_rep: str ) -> None:

        reg_btn = self.driver.find_element(*RegLocators.reg_btn)
        reg_btn.click()
        name = self.driver.find_element(*RegLocators.first_name)
        name.send_keys(nameu)
        last_user_name = self.driver.find_element(*RegLocators.last_name)
        last_user_name.send_keys(last)
        user_mail = self.driver.find_element(*RegLocators.regi_mail)
        user_mail.send_keys(reg_mail)
        user_passw = self.driver.find_element(*RegLocators.regi_pwd)
        user_passw.send_keys(reg_pwd)
        user_confpwd = self.driver.find_element(*RegLocators.regi_repassw)
        user_confpwd.send_keys(reg_pwd_rep)
        choice_reg = self.driver.find_element(*RegLocators.region)
        choice_reg.click()
        choice_reg.send_keys(Keys.BACKSPACE * 8)
        choice_reg.send_keys(region_name)
        submit = self.driver.find_element(*RegLocators.subm_btn)
        submit.click()

