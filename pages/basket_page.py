from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_empty_basket()
        self.should_be_empty_basket_message()
        self.should_not_add_in_basket_after_is_empty_message()

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.IS_BASKET_EMPTY), "Basket not empty"

    def should_be_empty_basket_message(self):
        assert "Your basket is empty" in self.browser.find_element(
            *BasketPageLocators.ADD_MESSAGE).text, "Basket not empty"

    def should_not_add_in_basket_after_is_empty_message(self):
        assert self.is_disappeared(*BasketPageLocators.IS_BASKET_EMPTY), "Basket not empty"
