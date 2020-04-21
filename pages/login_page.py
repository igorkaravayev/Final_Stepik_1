from .base_page import BasePage
from .locators import LoginPageLocators
import time
import math


class LoginPage(BasePage):
    def should_be_login_page(self, browser):
        self.should_be_login_url(browser)
        self.should_be_login_form(browser)
        self.should_be_register_form(browser)

    def should_be_login_url(self, browser):
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login url is not presented"
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        login_link.click()
        assert "login" in self.browser.current_url, "There is not login in url"
   
    def should_be_login_form(self, browser):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
    
    def should_be_register_form(self, browser):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        conf_password = self.browser.find_element(*LoginPageLocators.CONF_PASSWORD_FIELD)
        conf_password.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.BUTTON)
        button.click()

    def logout_user(self, browser):
        logout = self.browser.find_element(*LoginPageLocators.LOGOUT_BUTTON)
        logout.click()


