#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .pages.product_page import ProductPage
import time
import pytest

LINK = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
#LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
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
def test_should_add_product_to_cart(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.should_add_product_to_cart()
    time.sleep(1)
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.should_check_product_in_cart()
    page.should_check_price_in_cart()
    
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.should_add_product_to_cart()
    time.sleep(1)    
    page.tyu()
    
def test_guest_cant_see_success_message(browser): 
    page = ProductPage(browser, LINK)
    page.open()  
    page.tyu()
    
def test_message_disappeared_after_adding_product_to_basket(browser): 
    page = ProductPage(browser, LINK)
    page.open()
    page.should_add_product_to_cart()
    time.sleep(1)  
    page.ert()
    
