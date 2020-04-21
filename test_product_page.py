import pytest
from .pages.product_page import ProductPage
from .pages.product_page import PromoOffer
import time
from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

 
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_optened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_basket_page()    

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page() 

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


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

@pytest.mark.parametrize('promo_offer', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(self, browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = PromoOffer(browser, link)
    page.open()
    page.product_should_be_in_stock() # Check that product in stock
    page.add_product_to_basket() # Check that "Buy button" are present and buy product
    page.should_be_product_name_same() # Check that name in basket and bought product is the same 
    page.should_be_product_price_same() # Check that price in basket and bought product is the same

@pytest.mark.need_review
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        self.page = LoginPage(browser, self.link)
        self.page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "Abc"
        self.page.register_new_user(email, password)
        self.page.should_be_authorized_user()
        yield 
        self.page.logout_user(browser)
        self.page.should_be_login_page(browser)           

    def test_user_cant_see_success_message(self, browser):    
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.parametrize('promo_offer', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
    def test_user_can_add_product_to_basket(self, browser, promo_offer):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
        page = PromoOffer(browser, link)
        page.open()
        page.product_should_be_in_stock() # Check that product in stock
        page.add_product_to_basket() # Check that "Buy button" are present and buy product
        page.should_be_product_name_same() # Check that name in basket and bought product is the same 
        page.should_be_product_price_same() # Check that price in basket and bought product is the same

    



