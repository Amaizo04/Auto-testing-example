from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket_button(self):
        self.should_be_product_name()
        self.should_be_price_of_product()
        self.should_be_add_to_basket_button()
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_to_basket_button.click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "'Add to basket' button not found"

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "product name not found"

    def should_be_price_of_product(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "product price not found"

    def should_be_match_product_name_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text
        assert product_price == price_in_basket, "product price does not match"
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
        assert product_name == product_name_in_basket, "Product name does not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.PRODUCT_NAME_IN_BASKET), "Success message is presented, but should not be"

    def should_disappear_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.PRODUCT_NAME_IN_BASKET), "Success message is presented, but should not be"
