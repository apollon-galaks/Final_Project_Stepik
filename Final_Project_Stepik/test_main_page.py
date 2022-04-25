from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.locators import MainPageLocator
from .pages.locators import BasePageLocators
import pytest



@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser,url)
    page.open()
    page.solve_quiz_and_get_code()
    page.is_not_element_present(*MainPageLocator.SUCCESS_MESSAGE)

def test_guest_cant_see_success_message(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser,url)
    page.open()
    page.is_not_element_present(*MainPageLocator.SUCCESS_MESSAGE)

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser,url)
    page.open()
    page.solve_quiz_and_get_code()
    page.is_disappeared(*MainPageLocator.SUCCESS_MESSAGE)
    
@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_should_see_login_link_on_product_page(self, browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = MainPage(browser,url)
        page.open()
        page.should_be_login_link()

    @pytest.mark.xfail
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = MainPage(browser,url)
        page.open()
        page.go_to_login_page()
    


        page = MainPage(browser,url)
        page.open()
        page.should_be_login_link()

    @pytest.mark.skip
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = MainPage(browser,url)
        page.open()
        page.go_to_login_page()
    

