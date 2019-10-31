#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

LINK = 'http://selenium1py.pythonanywhere.com/'

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    
def test_guest_should_see_login_link(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.should_be_login_link()
    
@pytest.mark.test
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, LINK)
    page.open()
    page.go_to_basket_page()
    page.should_be_no_item_in_basket()
    page.should_be_empty_basket_message()
    
    
