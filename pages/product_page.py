from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .base_page import BasePage
import pytest
import time



class ProductPage(BasePage):
    
    def should_be_buy(self, browser):
        self.product_should_be_in_stock()
        self.add_product_to_basket()
        self.should_be_product_name_same()
        self.should_be_product_price_same()     

    def product_should_be_in_stock(self):
        assert self.is_element_present(*ProductPageLocators.IN_STOCK), "Product out of stock"

    def add_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PAGE), "Buy button is not presented"
        link = self.browser.find_element(*ProductPageLocators.PRODUCT_PAGE)
        link.click()  
        self.solve_quiz_and_get_code()
        
    def should_be_product_name_same(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        print(product_name, product_name_in_basket)
        assert product_name.text == product_name_in_basket.text, "Name of the product is not the same"

    def should_be_product_price_same(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET)
        assert product_price.text == product_price_in_basket.text, "Price of the product is not the same"



    