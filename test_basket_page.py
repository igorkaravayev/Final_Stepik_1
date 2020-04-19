import pytest
from .pages.basket_page import BasketPage
import time
from .pages.base_page import BasePage

@pytest.mark.xfail(reason="Negativ test for success add product")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = BasketPage(browser, link)
    page.open()
    page.should_not_be_success_message_after_buy()

def test_guest_cant_see_success_message(browser):    
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = BasketPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="Negativ test for an acspected disappeared success after add product")
def test_message_disappeared_after_adding_product_to_basket(browser):    
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = BasketPage(browser, link)
    page.open()
    page.should_disappeared_success_message()


