import pytest
import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

@pytest.mark.need_review
class TestNeedReview():
    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_button_add_to_basket()
        page.add_to_cart()
        page.should_be_add_message()
        page.cart_cost_should_be_equal_price_of_the_product()
        page.names_of_products_should_be_equal()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_any_item_in_basket()
        basket_page.should_be_empty_text()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

@pytest.mark.test_user_setup
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = MainPage(browser, link)
        page.open()
        login_page = LoginPage(browser, browser.current_url)
        input_email = str(time.time()) + "@fakemail.org"
        input_pass = "sdkfhsjkfsdf"
        login_page.register_new_user(input_email, input_pass)
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_button_add_to_basket()
        page.add_to_cart()
        page.should_be_add_message()
        page.cart_cost_should_be_equal_price_of_the_product()
        page.names_of_products_should_be_equal()