link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
def test_check_basket_button_exists(browser):
    browser.get(link)
    message = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert "Añadir al carrito" in message.text