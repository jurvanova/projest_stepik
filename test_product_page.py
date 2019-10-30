#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .pages.product_page import ProductPage
import time

#LINK = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'

def test_should_add_product_to_cart(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.should_add_product_to_cart()
    time.sleep(2)
    page.solve_quiz_and_get_code()
    time.sleep(5)
    page.should_check_product_in_cart()
    page.should_check_price_in_cart()
    
