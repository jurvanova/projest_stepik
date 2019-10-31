from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .locators import BasePageLocators
import math

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        
    def open(self):
        self.browser.get(self.url)
    
    def go_to_login_page(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
        
    def go_to_basket_page(self):
        self.browser.find_element(*BasePageLocators.BASKET_LINK).click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
        
    def is_element_present(self, how, what):
        try:
            WebDriverWait(self.browser, 3).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True
        
    def is_disappeared(self, how, what):
        try:
            WebDriverWait(self.browser, 3, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True
    
    def element_click(self, how, what):
        try:
            WebDriverWait(self.browser, 3).until(
                EC.presence_of_element_located((how, what))
            ).click()
        except TimeoutException:
            return False
        return True
                
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    
    
