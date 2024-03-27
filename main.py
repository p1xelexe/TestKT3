import time
import allure
import logging
from PageObjects.home import MainPage
from PageObjects.product import ProductPage
from PageObjects.registration import RegistrationPage
from conf import *
from conftest import *

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('log.txt')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


@allure.title("Screen test")
def screen(driver):
    logger.info("Starting screen test")
    driver.get(website)
    time.sleep(1)
    main_page = MainPage(driver)
    main_page.click(MainPage.PRODUCTS[0])
    time.sleep(1)
    product_page = ProductPage(driver)
    product_page.click(ProductPage.MAIN_PICTURE)
    time.sleep(1)
    product_page.kaka(3)
    time.sleep(2)
    logger.info("Screen test completed")


@allure.title("Cart test")
def korzina(driver):
    logger.info("Starting cart test")
    driver.get(website)
    time.sleep(3)
    main_page = MainPage(driver)
    main_page.click(MainPage.PRODUCTS_BUTTON_BUY[0])
    main_page.click(MainPage.PRODUCTS_BUTTON_BUY[1])
    main_page.click(MainPage.BUTTON_CART)
    time.sleep(3)
    logger.info("Cart test completed")


@allure.title("Popup test")
def popup(driver):
    logger.info("Starting popup test")
    driver.get(website)
    time.sleep(3)
    main_page = MainPage(driver)
    main_page.click(MainPage.DROPDOWN_PC)
    main_page.click(MainPage.LI_PC)
    time.sleep(3)
    logger.info("Popup test completed")


@allure.title("Registration test")
def registration(driver):
    logger.info("Starting registration test")
    driver.get(website)
    main_page = MainPage(driver)
    main_page.click(MainPage.BUTTON_REGLOG)
    main_page.click(MainPage.BUTTON_REGISTER)
    registration_page = RegistrationPage(driver)
    registration_page.registration()
    registration_page.click(RegistrationPage.BUTTON_TRUE_SUBNEWS)
    registration_page.click(RegistrationPage.BUTTON_ACCEPTANCE)
    registration_page.click(RegistrationPage.BUTTON_NEXT)
    time.sleep(3)
    logger.info("Registration test completed")


@allure.title("Search test")
def search(driver):
    logger.info("Starting search test")
    driver.get(website)
    main_page = MainPage(driver)
    main_page.Pinput(MainPage.INPUT_SEARCH, "search")
    main_page.enter()
    time.sleep(3)
    logger.info("Search test completed")


@allure.title("Favorites test")
def favorites(driver):
    logger.info("Starting favorites test")
    driver.get(website)
    time.sleep(3)
    main_page = MainPage(driver)
    index = main_page.random(MainPage.PRODUCTS)
    main_page.click(MainPage.PRODUCTS_BUTTON_FAVORITE[index])
    time.sleep(3)
    logger.info("Favorites test completed")


@allure.title("Cams test")
def cams(driver):
    logger.info("Starting cams test")
    driver.get(website)
    time.sleep(3)
    main_page = MainPage(driver)
    main_page.click(MainPage.PRODUCTS[MainPage.LAST_INDEX])
    product_page = ProductPage(driver)
    product_page.click(ProductPage.SELECT_OPTION_COLOR)
    product_page.click(ProductPage.BUTTON_BUY)
    logger.info("Cams test completed")


@allure.title("Tablet test")
def tablet(driver):
    logger.info("Starting tablet test")
    driver.get(website)
    time.sleep(3)
    main_page = MainPage(driver)
    main_page.click(MainPage.DROPDOWN_TABLET)
    main_page.click(MainPage.PRODUCT_TABLET)
    product_page = ProductPage(driver)
    product_page.click(ProductPage.BUTTON_BUY)
    logger.info("Tablet test completed")


@allure.title("HTC test")
def HTC(driver):
    logger.info("Starting HTC test")
    driver.get(website)
    time.sleep(3)
    main_page = MainPage(driver)
    main_page.click(MainPage.DROPDOWN_TELEPHONE_HTC)
    main_page.click(MainPage.PRODUCT_TELEPHONE_HTC)
    product_page = ProductPage(driver)
    product_page.click(ProductPage.BUTTON_BUY)
    logger.info("HTC test completed")


@allure.title("Review test")
def rew(driver):
    logger.info("Starting review test")
    driver.get(website)
    main_page = MainPage(driver)
    main_page.click(MainPage.PRODUCTS[0])
    product_page = ProductPage(driver)
    product_page.click(ProductPage.BUTTON_REVIEW)
    product_page.Pinput(ProductPage.INPUT_NAME_REVIEW, first)
    product_page.Pinput(ProductPage.INPUT_REVIEW, reviewt)
    product_page.click(ProductPage.BUTTON_REVIEW_MARK[4])
    product_page.click(ProductPage.BUTTON_NEXT_REVIEW)
    time.sleep(3)
    logger.info("Review test completed")


screen(driver)
korzina(driver)
search(driver)
registration(driver)
popup(driver)
favorites(driver)
cams(driver)
tablet(driver)
HTC(driver)
rew(driver)
