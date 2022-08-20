from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#id_login-username")
    PASSWORD_FORM = (By.CSS_SELECTOR, "#id_login-password")

class ProducktLocators():
    BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ADDET_TO_BASKET = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) strong")
    NAME_PRODUCKT = (By.TAG_NAME, "h1")
    PRISE_IN_BASKET = (By.CSS_SELECTOR, "#messages > .alert:nth-child(3) strong")
    PRISE_PRODUKT = (By.CSS_SELECTOR, ".col-sm-6 .price_color")