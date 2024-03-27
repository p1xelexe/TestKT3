import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

website = "https://demo-opencart.ru"

service = ChromeService()
driver = webdriver.Chrome(service=service)


def pyte(parser):
    parser.addoption("--browser", default="chrome")


@pytest.fixture
def drivers(request):
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(website)
    request.addfinalizer(driver.quit)

    return driver
