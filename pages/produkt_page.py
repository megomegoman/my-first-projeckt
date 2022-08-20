from .base_page import BasePage
from .locators import ProducktLocators

class ProduktPage(BasePage):
    def add_to_bascet(self):
        self.browser.find_element(*ProducktLocators.BASKET).click()

    def added_to_your_basket(self):
        self.messenge = self.browser.find_element(*ProducktLocators.ADDET_TO_BASKET)
        self.name_produkt = self.browser.find_element(*ProducktLocators.NAME_PRODUCKT)
        assert self.name_produkt.text in self.messenge.text, "wrong product added to basket"

    def price_in_the_basket(self):
        self.messenge_price = self.browser.find_element(*ProducktLocators.PRICE_IN_BASKET)
        self.price_produkt = self.browser.find_element(*ProducktLocators.NAME_PRODUCKT)
        assert self.price_produkt.text in self.messenge_price.text, "the price does not match the value of the product"

    def finding_a_product_in_the_basket(self):
        self.added_to_your_basket()
        self.price_in_the_basket()
