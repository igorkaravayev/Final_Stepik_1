from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from .locators import BasePageLocators
import math


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    def open(self):
        self.browser.get(self.url)
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")  

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
            until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
    
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_not_be_login(self):
        assert not self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is presented"
    
    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_PAGE)
        link.click()
        empty_basket = self.browser.find_element(*BasePageLocators.EMPTY_BASKET)
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET),\
        "Busket is not empty"
        language = self.browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")
        languages = {
        "ar": "سلة التسوق فارغة",
        "ca": "La seva cistella està buida.",
        "cs": "Váš košík je prázdný.",
        "da": "Din indkøbskurv er tom.",
        "de": "Ihr Warenkorb ist leer.",
        "en": "Your basket is empty.",
        "el": "Το καλάθι σας είναι άδειο.",
        "es": "Tu carrito esta vacío.",
        "fi": "Korisi on tyhjä",
        "fr": "Votre panier est vide.",
        "it": "Il tuo carrello è vuoto.",
        "ko": "장바구니가 비었습니다.",
        "nl": "Je winkelmand is leeg",
        "pl": "Twój koszyk jest pusty.",
        "pt": "O carrinho está vazio.",
        "pt-br": "Sua cesta está vazia.",
        "ro": "Cosul tau este gol.",
        "ru": "Ваша корзина пуста",
        "sk": "Váš košík je prázdny",
        "uk": "Ваш кошик пустий.",
        "zh-cn": "Your basket is empty."
}
        assert languages[language] in empty_basket.text, "No text"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"