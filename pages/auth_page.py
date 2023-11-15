from pages.main_page import MainPage
from locators import AuthLocators
class AuthPage(MainPage):

    def login_user(self, query: str, value: str) -> None:
        login = self.driver.find_element(*AuthLocators.user_name)
        login.send_keys(query)
        password = self.driver.find_element(*AuthLocators.user_pwd)
        password.send_keys(value)
        login_btn = self.driver.find_element(*AuthLocators.log_btn)
        login_btn.click()

    def login_user_from_Belarus(self, query: str, value: str) -> None:
        login = self.driver.find_element(*AuthLocators.user_name)
        login.send_keys(query)
        password = self.driver.find_element(*AuthLocators.user_pwd)
        password.send_keys(value)


    def help_menu(self) -> None:
        help_button = self.driver.find_element(*AuthLocators.help_btn)
        help_button.click()

    def empty_tel(self) -> None:
        button = self.driver.find_element(*AuthLocators.fgt_btn)
        button.click()
        forward = self.driver.find_element(*AuthLocators.forgot_forward)
        forward.click()

    def wrong_tel(self, value) -> None:
        button = self.driver.find_element(*AuthLocators.fgt_btn)
        button.click()
        user = self.driver.find_element(*AuthLocators.user_name)
        user.send_keys(value)
        forward = self.driver.find_element(*AuthLocators.forgot_forward)
        forward.click()


