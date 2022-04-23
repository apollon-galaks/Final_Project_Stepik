from socket import timeout
import numpy as np
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException



class BasePage():
    def __init__(self, browser, url, timeout = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True


    def solve_quiz_and_get_code(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
        

    def open(self):
        self.browser.get(self.url)