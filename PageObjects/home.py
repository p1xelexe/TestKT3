from PageObjects.base import BasePage
from selenium.webdriver.common.by import By
from conf import *


class MainPage(BasePage):
    INPUT_SEARCH = (By.CSS_SELECTOR, "div.container div.row div.col-sm-5 div.input-group > input.form-control.input-lg")
    BUTTON_CART_TOTAL = (By.CSS_SELECTOR, "#cart-total")
    BUTTON_CART = (By.XPATH, "//body/nav[@id='top']/div[1]/div[1]/ul[1]/li[4]/a[1]")
    BUTTON_REGLOG = (
        By.CSS_SELECTOR, "div.container div.nav.pull-right ul.list-inline li.dropdown:nth-child(2) > a.dropdown-toggle"
    )

    BUTTON_REGISTER = (By.LINK_TEXT, "Регистрация")
    BUTTON_LOGIN = (By.LINK_TEXT, "Авторизация")
    BUTTON_HOME = (By.LINK_TEXT, "Интернет магазин Opencart")

    DROPDOWN_TABLET = (By.LINK_TEXT, "Планшеты")
    PRODUCT_TABLET = (By.LINK_TEXT, "Samsung Galaxy Tab 10.1")

    DROPDOWN_TELEPHONE_HTC = (By.LINK_TEXT, "Телефоны")
    PRODUCT_TELEPHONE_HTC = (By.LINK_TEXT, "HTC Touch HD")

    DROPDOWN_PC = (By.LINK_TEXT, "Компьютеры")
    LI_PC = (By.LINK_TEXT, "PC (0)")

    PRODUCTS = [
        (By.CSS_SELECTOR, product.format(str(i), element))
        for i in range(1, 5)
    ]

    PRODUCTS_BUTTON_BUY = [
        (By.CSS_SELECTOR, product.format(str(i), button_buy))
        for i in range(1, 5)
    ]

    PRODUCTS_BUTTON_FAVORITE = [
        (By.CSS_SELECTOR, product.format(str(i), button_fav))
        for i in range(1, 5)
    ]

    LAST_INDEX = len(PRODUCTS) - 1
