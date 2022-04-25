from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
from.pages.locators import MainPageLocator
from .pages.login_page import LoginPage
import time

import pytest

@pytest.mark.need_review
class TestGuestAddToBasketFromProductPage():
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser,url)
        page.open()
        page.is_not_element_present(*ProductPageLocators.LOGIN_FROM_PP)


    def test_guest_cant_see_success_message(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser,url)
        page.open()
        page.is_not_element_present(*ProductPageLocators.ADD_TO_CART)
        
    def test_guest_can_add_product_to_basket(self, browser):
        url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, url)
        page.open()
        page.add_to_cart(*MainPageLocator.LOGIN_LINK)



@pytest.mark.need_review
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page.register_new_user(email=email, password=password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser,url)
        page.open()
        page.is_not_element_present(*ProductPageLocators.ADD_TO_CART)
    
    def test_user_can_add_product_to_basket(self, browser):
        url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, url)
        page.open()
        page.add_to_cart(*MainPageLocator.LOGIN_LINK)
