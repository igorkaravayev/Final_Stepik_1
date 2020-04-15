from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_promo_for_book() # Check that "promo" are in the URL
    page.product_should_be_in_stock() # Check that product in stock
    page.add_product_to_basket() # Check that "Buy button" are present and buy product
    page.should_be_product_name_same() # Check that name in basket and bought product is the same 
    page.should_be_product_price_same() # Check that price in basket and bought product is the same


  