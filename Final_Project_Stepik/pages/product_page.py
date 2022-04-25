from .base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(ProductPage, self).__init__(*args, **kwargs)
