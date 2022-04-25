from .base_page import BasePage
from .locators import LoginLocators

class LoginPage(BasePage):

    def register_new_user(self, email, password):
        
        input_email = self.browser.find_element(*LoginLocators.EMAIL)
        input_email.send_keys(email)
        input_pass = self.browser.find_element(*LoginLocators.PASS)
        input_pass.send_keys(password)
        conf_pass = self.browser.find_element(*LoginLocators.CONF_PASS)
        conf_pass.send_keys(password)
        reg_but = self.browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div[2]/form/button')
        self.browser.execute_script("arguments[0].scrollIntoView();", reg_but)
        reg_but.click()
