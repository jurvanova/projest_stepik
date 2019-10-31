from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

import time
import pytest


LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
LINK_PROMO = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'

'''
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
'''

@pytest.mark.need_review                                
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, LINK_PROMO)
    page.open()
    page.should_add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_check_product_in_cart()
    page.should_check_price_in_cart()
    
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK_PROMO)
    page.open()
    page.should_add_product_to_cart()
    time.sleep(1)    
    page.should_not_be_success_message()
    
def test_guest_cant_see_success_message(browser): 
    page = ProductPage(browser, LINK_PROMO)
    page.open()  
    page.should_not_be_success_message()
    
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser): 
    page = ProductPage(browser, LINK_PROMO)
    page.open()
    page.should_add_product_to_cart()
    time.sleep(1)  
    page.should_not_be_message()
    

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.should_be_login_link()
    
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.go_to_login_page()
    login_page = BasePage(browser, browser.current_url)
    login_page.should_be_login_link()
    
@pytest.mark.need_review    
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, LINK)
    page.open()
    page.go_to_basket_page()
    page.should_be_no_item_in_basket()
    page.should_be_empty_basket_message()

@pytest.mark.login_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, LINK_PROMO)
        page.open()
        page.go_to_login_page()
        page.register_new_user(f'test{str(time.time())}@test.com', 'pytest-rerunfailures')
        page.should_see_succes_registred_message()
        
    @pytest.mark.need_review    
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, LINK_PROMO)
        page.open()
        page.should_add_product_to_cart()
        page.solve_quiz_and_get_code()
        page.should_be_authorized_user()
        page.should_check_product_in_cart()
        page.should_check_price_in_cart()
    
    def test_guest_cant_see_success_message(self, browser): 
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        page = ProductPage(browser, LINK_PROMO)
        page.open()  
        page.should_not_be_success_message()
    
