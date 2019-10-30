from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException 
from selenium.common.exceptions import TimeoutException 
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):
    
    def should_add_product_to_cart(self):
        self.should_check_cart_button()
        self.element_click(*ProductPageLocators.ADD_TO_BASKET)

    def should_check_product_in_cart(self):
        PRODUCT_NAME = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_SELECT).text
        print(PRODUCT_NAME)
        self.should_check_product_name(PRODUCT_NAME)
        
    def should_check_price_in_cart(self):
        PRODUCT_PRICE = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_SELECT).text
        print(PRODUCT_PRICE)
        self.should_check_product_price(PRODUCT_PRICE)
        
        
        
    def tyu(self):
        self.should_not_be_success_message()
        
    def ert(self):
        self.should_not_be_message()
        

    def should_check_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), 'Button add to cart is not found'
    
    def should_check_product_name(self, param):
        assert param == self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_MESSAGE).text, 'Product name is incorrect'
        
    def should_check_product_price(self, param):
        assert param == self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_MESSAGE).text, 'Price of product is incorrect'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),  f"Success message is presented, but should not be"
           
    def should_not_be_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), f"Success message is not presented, but should be"
