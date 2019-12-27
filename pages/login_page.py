from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self):
        email = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        email.send_keys(str(time.time()) + "@testmail.org")
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), "Email field not found"
        password = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        password.send_keys("stepik27122019")
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD), "Password field not found"
        repeat_password = self.browser.find_element(*LoginPageLocators.REPEAT_REG_PASSWORD)
        repeat_password.send_keys("stepik27122019")
        assert self.is_element_present(*LoginPageLocators.REPEAT_REG_PASSWORD), "Repeat-password field not found"
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_button.click()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "word 'login' not found"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form not found"
