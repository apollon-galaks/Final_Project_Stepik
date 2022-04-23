from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    url = '(http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, url)
    page.open()
    page.add_to_cart()
