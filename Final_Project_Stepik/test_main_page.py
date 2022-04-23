from .pages.main_page import MainPage

def test_guest_should_see_login_link(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser,url)
    page.open()
    page.solve_quiz_and_get_code()
    page.cart_price_and_book_name()


"""def test_guest_can_go_to_login_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=midsummer"
    page = MainPage(browser, url)
    page.open()
    page.go_to_login_page()"""