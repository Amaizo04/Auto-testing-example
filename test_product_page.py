import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.basket_page import BasePage
from pages.login_page import LoginPage


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        self.page = BasePage(browser, link)
        self.page.open()
        self.login_page = LoginPage(browser, browser.current_url)
        self.reg_page = self.login_page.go_to_login_page()
        self.new_user = self.login_page.register_new_user()
        self.check_new_user = self.login_page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.reg_page)
        new_user = ProductPage(browser, self.new_user)
        check_new_user = ProductPage(browser, self.check_new_user)
        self.page.open()
        product_page = ProductPage(browser, browser.current_url)
        product_page.add_to_basket_button()
        self.page.solve_quiz_and_get_code()
        product_page.should_be_match_product_name_price()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    page = BasePage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_basket_button()
    page.solve_quiz_and_get_code()
    product_page.should_be_match_product_name_price()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
