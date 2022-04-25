import numpy as np
from .locators import BasePageLocators
from .locators import MainPageLocator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException



class BasePage():
    def __init__(self, browser, url, timeout = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON),\
             "User icon is not presented"\
                "probably unauthorised user"

    def add_to_cart(self, how, what):
        login_link = self.browser.find_element(how, what)
        self.browser.execute_script("arguments[0].scrollIntoView();", login_link)
        login_link.click()


    def solve_quiz_and_get_code(self):
        login_link = self.browser.find_element(*MainPageLocator.LOGIN_LINK)
        self.browser.execute_script("arguments[0].scrollIntoView();", login_link)
        login_link.click()
        
        alert = self.browser.switch_to.alert 
        assert alert is not None, 'No Alert!'

        x = alert.text.split(" ")[2]
        answer = str(np.log(abs((12 * np.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*MainPageLocator.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_not_element_present(*MainPageLocator.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"
    
    def cart_price_and_book_name(self):
        
        self.browser.implicitly_wait(10)
        chld = self.browser.window_handles[0]
        self.browser.switch_to.window(chld)

        book_name = self.browser.find_element(*MainPageLocator.BOOK_NAME)
        assert book_name.text == "Coders at Work", "No book!"
        book = book_name.text
        print("Book name is " + book)
        cart_price = self.browser.find_element(*MainPageLocator.CART_PRICE)
        assert cart_price.text == '£19.99', "No price!"
        price = cart_price.text
        print("Cart price is " + price)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINKK_INVALID)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINKK),\
             "Login link is not presented"
    
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    
    def open(self):
        self.browser.get(self.url)
