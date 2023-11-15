from pages.main_page import MainPage
from locators import AuthLocators


class AuthPage(MainPage):

    def login_input_data(self, query):
        login = self.driver.find_element(*AuthLocators.user_name)
        login.send_keys(query)

    def password_input_data(self, value):
        password = self.driver.find_element(*AuthLocators.user_pwd)
        password.send_keys(value)

    def login_button_click(self):
        login_btn = self.driver.find_element(*AuthLocators.log_btn)
        login_btn.click()

    def help_button_click(self):
        help_button = self.driver.find_element(*AuthLocators.help_btn)
        help_button.click()

    def forgot_password_button_click(self):
        button = self.driver.find_element(*AuthLocators.fgt_btn)
        button.click()

    def forward_button_click(self):
        forward = self.driver.find_element(*AuthLocators.forgot_forward)
        forward.click()

    def login_user(self, query: str, value: str) -> None:
        self.login_input_data(query)
        self.password_input_data(value)
        self.login_button_click()

    def login_user_from_Belarus(self, query: str, value: str) -> None:
        self.login_input_data(query)
        self.password_input_data(value)

    def help_menu(self) -> None:
        self.help_button_click()

    def empty_tel(self) -> None:
        self.forgot_password_button_click()
        self.forward_button_click()

    def wrong_tel(self, value) -> None:
        self.forgot_password_button_click()
        self.login_input_data(value)
        self.forward_button_click()

