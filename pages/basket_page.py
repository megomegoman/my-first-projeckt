from .base_page import BasePage
from .locators import BasketPage

class BasketPage(BasePage):
    def no_products_in_the_basket(self):
        assert self.is_not_element_present(*BasketPage.PRODUCT_IN_BASKET), "products in the basket, should not be"

    def message_that_the_basket_is_empty(self):
        assert self.is_element_present(*BasketPage.MESSAGE_BASKET_IS_EMPTY), "there is no message that the basket is empty"