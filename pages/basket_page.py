from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_no_item_in_basket(self):
        assert not self.is_element_present(*BasketPageLocators.BASKET_ITEM), 'Basket is not empty'
        
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE), 'Basket is not empty'
