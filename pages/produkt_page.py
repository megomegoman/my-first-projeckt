from .base_page import BasePage
from .locators import ProducktLocators

class ProduktPage(BasePage):
    #нажимаем кнопку "добавить в корзину"
    def add_to_bascet(self):
        self.browser.find_element(*ProducktLocators.BASKET).click()

    #Проверяем добавился ли продукт в корзину и тот ли это продукт
    def added_to_your_basket(self):
        assert self.is_element_present(*ProducktLocators.ADDET_TO_BASKET), "Message about adding is not presented"
        assert self.is_element_present(*ProducktLocators.NAME_PRODUCKT), "Product name is not presented"
        self.messenge = self.browser.find_element(*ProducktLocators.ADDET_TO_BASKET)
        self.name_produkt = self.browser.find_element(*ProducktLocators.NAME_PRODUCKT)
        assert self.name_produkt.text == self.messenge.text, "wrong product added to basket"

    #проверяем что цена товара соответствует цене товара в корзине
    def price_in_the_basket(self):
        assert self.is_element_present(*ProducktLocators.PRISE_IN_BASKET), "no message about the cost of the item added to the basket"
        assert self.is_element_present(*ProducktLocators.PRISE_PRODUKT), "no product price"
        self.messenge_price = self.browser.find_element(*ProducktLocators.PRISE_IN_BASKET)
        self.price_produkt = self.browser.find_element(*ProducktLocators.PRISE_PRODUKT)
        assert self.price_produkt.text == self.messenge_price.text, "the price does not match the value of the product"

    def finding_a_product_in_the_basket(self):
        self.added_to_your_basket()
        self.price_in_the_basket()
