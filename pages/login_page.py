from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'URL isn\'t valid'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_SELECTOR), 'Login form isn\'t presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_SELECTOR), 'Registred form isn\'t presented'

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
        
    def should_see_succes_registred_message(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_MESSAGE_SUCCES), 'Registred fails!'

        
