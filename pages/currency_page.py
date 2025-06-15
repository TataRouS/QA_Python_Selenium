from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CurrencyPage(BasePage):
    CURRENCY_DROPDOWN = (By.XPATH, '//*[@id="form-currency"]/div/a')
    CURRENCY_LIST = (By.XPATH, '//*[@id="form-currency"]/div/ul/li')
