from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_START = (By.CSS_SELECTOR, '.col-sm-7.h1')
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    
class LoginPageLocators():
    FORM_SELECTOR = (By.CSS_SELECTOR, '#login_form')
    REGISTER_SELECTOR = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[value="Register"]')
    REGISTER_MESSAGE_SUCCES = (By.CSS_SELECTOR, '.alertinner.wicon')
    
class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME_SELECT = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE_SELECT = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_NAME_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(1) strong')
    PRODUCT_PRICE_MESSAGE = (By.CSS_SELECTOR, '#messages p:nth-child(1) strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div')
    
class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, '.basket-items')
    BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner>p')
