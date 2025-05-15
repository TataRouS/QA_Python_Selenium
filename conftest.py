import pytest
from selenium import webdriver

from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions


def pytest_addoption(parser):
    parser.addoption("--browser", help="browser to run tests")
    parser.addoption("--drivers", help="drivers storage", default="Users/tata_rous/Downloads")
    parser.addoption("--headless", action = "store_true", help="headless")
    parser.addoption("--base_url", help="Base application url", default="192.168.0.10:8081")

@pytest.fixture(scope="session")
def base_url(request):
    return "http://" + request.config.getoption("--base_url")

@pytest.fixture()
def browser(request):
    driver = None
    browser_name = request.config.getoption("--browser")
    drivers_storage = request.config.getoption("--drivers")
    headless = request.config.getoption("--headless")

    if browser_name in ["ch", "chrome"]:
        options = ChromeOptions()
        if headless:
            options.add_argument("headless=new")
        driver = webdriver.Chrome(options=options)
    elif browser_name in ["ff", "firefox"]:
        options = FFOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    elif browser_name in ["ya", "yandex"]:
        options = ChromiumOptions()
        options.binary_location = "Users/tata_rous/Downloads/yandexdriver"
        if headless:
            options.add_argument("headless-new")

        driver = webdriver.Chrome(
            options = options,
            service = ChromiumService(executable_path=f"{drivers_storage}/yandexdriver"))

    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def catalog_page_url(request):
    return "http://" + request.config.getoption("--base_url") + "/en-gb/catalog/desktops"

@pytest.fixture(scope="session")
def login_page_url(request):
    return "http://" + request.config.getoption("--base_url") + "/en-gb?route=account/login"

@pytest.fixture(scope="session")
def product_page_url(request):
    return "http://" + request.config.getoption("--base_url") + "/en-gb/product/desktops/mac/imac"

@pytest.fixture(scope="session")
def register_account_page_url(request):
    return "http://" + request.config.getoption("--base_url") + "/en-gb?route=account/register"

# @pytest.fixture(scope="session")
# def change_currency(browser, base_url):
#     browser.get(base_url)
#     browser.find_element(By.XPATH, "//*[@id=\"form-currency\"]/div/a/i").click()
#     time.sleep(2) # Для демонстрации
#     drop_menu = browser.find_elements(By.XPATH, "//*[@id=\"form-currency\"]/div/ul/li")
#     euro = browser.find_element(By.XPATH, "//*[@id=\"form-currency\"]/div/ul/li[1]/a")
#     pound_sterling = browser.find_element(By.XPATH, "//*[@id=\"form-currency\"]/div/ul/li[1]/a")
#     us_dollar = browser.find_element(By.XPATH, "//*[@id=\"form-currency\"]/div/ul/li[1]/a")
#     for element in drop_menu:
#         if element.get_attribute(element.)