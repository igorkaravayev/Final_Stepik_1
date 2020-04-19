import pytest
from .pages.product_page import ProductPage
from .pages.product_page import PromoOffer
import time
from .pages.base_page import BasePage

@pytest.mark.xfail(reason="Negativ test for success add product")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message_after_buy()

def test_guest_cant_see_success_message(browser):    
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="Negativ test for an acspected disappeared success after add product")
def test_message_disappeared_after_adding_product_to_basket(browser):    
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_disappeared_success_message()

@pytest.mark.parametrize('promo_offer', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail, reason="Add book text fail"), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = PromoOffer(browser, link)
    page.open()
    
    page.product_should_be_in_stock() # Check that product in stock
    page.add_product_to_basket() # Check that "Buy button" are present and buy product
    
    promo = f"http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    assert str(promo) == browser.current_url, "There's no promo in the link" # Check that "promo" are in the URL

    page.should_be_product_name_same() # Check that name in basket and bought product is the same 
    page.should_be_product_price_same() # Check that price in basket and bought product is the same


