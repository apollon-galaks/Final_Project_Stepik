from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):


    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        #add_cart.click()