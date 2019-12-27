from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")
    MAIN_PAGE_LINK = (By.CSS_SELECTOR, "div.page_inner div div.col-sm-7 a")
    BASKET_PAGE_BUTTON = (By.CSS_SELECTOR, "span.btn-group a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "button[name=\"login_submit\"]")
    REG_FORM = (By.CSS_SELECTOR, "button[name=\"registration_submit\"]")
    REG_EMAIL = (By.CSS_SELECTOR, "input[name=\"registration-email\"]")
    REG_PASSWORD = (By.CSS_SELECTOR, "input[name=\"registration-password1\"]")
    REPEAT_REG_PASSWORD = (By.CSS_SELECTOR, "input[name=\"registration-password2\"]")
    REG_BUTTON = (By.CSS_SELECTOR, "button[name=\"registration_submit\"]")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, "div.alert-info strong")
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")


class BasketPageLocators:
    IS_BASKET_EMPTY = (By.CSS_SELECTOR, "#id_form-0-quantity")
    ADD_MESSAGE = (By.CSS_SELECTOR, "div#content_inner")
