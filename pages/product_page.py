from .base_page import BasePage
from .locators import ProductLocators

class ProductPage(BasePage):
    #нажимаем кнопку "добавить в корзину"
    def add_to_bascet(self):
        self.browser.find_element(*ProductLocators.BASKET).click()

    #Проверяем добавился ли продукт в корзину и тот ли это продукт
    def added_to_your_basket(self):
        assert self.is_element_present(*ProductLocators.ADDET_TO_BASKET), "Message about adding is not presented"
        assert self.is_element_present(*ProductLocators.NAME_PRODUCKT), "Product name is not presented"
        self.messenge = self.browser.find_element(*ProductLocators.ADDET_TO_BASKET)
        self.name_produkt = self.browser.find_element(*ProductLocators.NAME_PRODUCKT)
        assert self.name_produkt.text == self.messenge.text, "wrong product added to basket"

    #проверяем что цена товара соответствует цене товара в корзине
    def price_in_the_basket(self):
        assert self.is_element_present(*ProductLocators.PRISE_IN_BASKET), "no message about the cost of the item added to the basket"
        assert self.is_element_present(*ProductLocators.PRISE_PRODUKT), "no product price"
        self.messenge_price = self.browser.find_element(*ProductLocators.PRISE_IN_BASKET)
        self.price_produkt = self.browser.find_element(*ProductLocators.PRISE_PRODUKT)
        assert self.price_produkt.text == self.messenge_price.text, "the price does not match the value of the product"

    def finding_a_product_in_the_basket(self):
        self.added_to_your_basket()
        self.price_in_the_basket()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappered(*ProductLocators.SUCCESS_MESSAGE), \
            "Success message does not disappear, but should"

