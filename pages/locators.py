from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    
class LoginPageLocators():
    FORM_SELECTOR = (By.CSS_SELECTOR, '#login_form')
    REGISTER_SELECTOR = (By.CSS_SELECTOR, '#register_form')
    
class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME_SELECT = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE_SELECT = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_NAME_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(1) strong')
    PRODUCT_PRICE_MESSAGE = (By.CSS_SELECTOR, '#messages p:nth-child(1) strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#default')
