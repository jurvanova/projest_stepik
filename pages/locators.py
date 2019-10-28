from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    
class LoginPageLocators():
    FORM_SELECTOR = (By.CSS_SELECTOR, '#login_form')
    REGISTER_SELECTOR = (By.CSS_SELECTOR, '#register_form')
    
