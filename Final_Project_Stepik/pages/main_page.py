from .base_page import BasePage
from .locators import MainPageLocator
from selenium.webdriver.common.by import By
import numpy as np
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException

class MainPage(BasePage):

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
    def cart_price_and_book_name(self):
        
        self.browser.implicitly_wait(10)
        chld = self.browser.window_handles[0]
        self.browser.switch_to.window(chld)

        book_name = self.browser.find_element(*MainPageLocator.BOOK_NAME)
        assert book_name is not None, "No book!"
        book = book_name.text
        print("Book name is " + book)
        cart_price = self.browser.find_element(*MainPageLocator.CART_PRICE)
        assert cart_price is not None, "No price!"
        price = cart_price.text
        print("Cart price is " + price)




#/html/body/div[2]/div/div[1]/div[1]/div/strong --- Book name
#/html/body/div[2]/div/div[1]/div[3]/div/p[1]/strong --- Cart Price
            


    """def go_to_login_page(self):
    login_link.location_once_scrolled_into_view
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        #alert = self.browser.switch_to.alert
        #alert.accept()"""
    
    """def add_to_cart(self):
        self.browser.find_element(*MainPageLocators1.ADD_TO_CART)
        #add_cart.click()"""
        
    
