from selenium.webdriver.common.by import By


class MainPageLocator():
    LOGIN_LINK = (By.CSS_SELECTOR, '[class = "btn btn-lg btn-primary btn-add-to-basket"]')
    BOOK_NAME = (By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div/strong')
    CART_PRICE = (By.XPATH, '/html/body/div[2]/div/div[1]/div[3]/div/p[1]/strong')

"""class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, "[class = 'btn btn-lg btn-primary btn-add-to-basket']")"""