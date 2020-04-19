from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators
import pytest
import time



class BasketPage(BasePage):

    
    def should_not_be_success_message_after_buy(self):
        link = self.browser.find_element(*BasketPageLocators.PRODUCT_PAGE)
        link.click()
        assert not self.is_element_present(*BasketPageLocators.SUCCESS_MESSAGE),\
        "Success message is presented"

    def should_not_be_success_message(self):
        assert not self.is_element_present(*BasketPageLocators.SUCCESS_MESSAGE),\
        "Success message is not presented"    

    
    def should_disappeared_success_message(self):
        link = self.browser.find_element(*BasketPageLocators.PRODUCT_PAGE)
        link.click()
        assert self.is_disappeared(*BasketPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"
    

    