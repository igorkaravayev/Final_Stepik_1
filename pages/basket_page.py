from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators
import time 
    
class BasketPage(BasePage):  
    def go_to_basket_page(self):
        link = self.browser.find_element(*BasketPageLocators.BASKET_PAGE)
        link.click()
        empty_basket = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET)
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET),\
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