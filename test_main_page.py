import pytest
from .pages.base_page import BasePage

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = BasePage(browser, link)
    page.open()
    page.go_to_basket_page() #Check that guest cant see product in open basket from main page
    

