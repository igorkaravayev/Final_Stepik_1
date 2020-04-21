from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_PAGE = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
    PRODUCT_PAGE = (By.CSS_SELECTOR, ".btn-add-to-basket")

class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONF_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "#logout_link")

class ProductPageLocators():
    PRODUCT_PAGE = (By.CSS_SELECTOR, ".btn-add-to-basket")
    IN_STOCK = (By.CSS_SELECTOR, "p.instock.availability")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, ".alertinner > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alertinner  p strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".fade .alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
    PRODUCT_PAGE = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_PAGE = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_PAGE = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
    PRODUCT_PAGE = (By.CSS_SELECTOR, ".btn-add-to-basket")

    
