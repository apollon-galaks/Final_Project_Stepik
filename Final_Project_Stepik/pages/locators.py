from selenium.webdriver.common.by import By


class MainPageLocator():
    LOGIN_LINK = (By.CSS_SELECTOR, '[class = "btn btn-lg btn-primary btn-add-to-basket"]')
    BOOK_NAME = (By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div/strong')
    CART_PRICE = (By.XPATH, '/html/body/div[2]/div/div[1]/div[3]/div/p[1]/strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(1)')

class BasePageLocators():
    LOGIN_LINKK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINKK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, "[class = 'btn btn-lg btn-primary btn-add-to-basket']")

class LoginLocators():
    REG = (By.XPATH, '/html/body/div[1]/div[2]/div/ul/li/a')
    EMAIL = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div/div[2]/form/div[1]/div/input')
    PASS = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div/div[2]/form/div[2]/div/input')
    CONF_PASS = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div/div[2]/form/div[3]/div/input')
