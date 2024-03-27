import time

from selenium.webdriver.common.by import By


class AlertElement:
    THIS = (
        By.CSS_SELECTOR, ".body:nth-child(2) div.container:nth-child(4) > div.alert.alert-success.alert-dismissible")
    CART = (By.LINK_TEXT, "shopping cart")

    def __init__(self, driver):
        self.driver = driver

    def alert_htc(self, element_locator):
        if "HTC Touch HD добавлен в корзину покупок!" in self.find_element(*element_locator.THIS).text:
            print("HTC добавлен в корзину")
            self.driver.get("https://demo-opencart.ru/index.php?route=checkout/cart")
        time.sleep(4)

    def alert_tablet(self, element_locator):
        if "Samsung Galaxy Tab 10.1 добавлен в корзину покупок!" in self.find_element(*element_locator.THIS).text:
            print("Samsung добавлен в корзину")
            self.driver.get("https://demo-opencart.ru/index.php?route=checkout/cart")
        time.sleep(4)
