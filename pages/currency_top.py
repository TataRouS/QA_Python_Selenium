from selenium.webdriver.common.by import By
from pages.admin_login_page import AdminLoginPage
import time
import random


class TopPage(AdminLoginPage):
    # Локаторы
    CURRENCY = (By.XPATH, '//*[@id="form-currency"]/div/a')
    CURRENCY_SYMBOL = (By.XPATH, '//*[@id="form-currency"]/div/a/strong')
    DROP_CURRENCY_MENU = (By.XPATH, '//*[@id="form-currency"]/div/ul')

    def change_currency(self):
        # Клик по кнопке выбора валюты
        self.click_on_element(self.CURRENCY)
        time.sleep(3)
        drop_menu = self.find_elements(self.DROP_CURRENCY_MENU)

        # Выбираем новую валюту (по первому символу)
        drop_element = random.choice(drop_menu)
        drop_element.click()
        return self.find_element(self.CURRENCY_SYMBOL).text

    def get_previous_currency(self):
        return self.find_element(self.CURRENCY_SYMBOL).text
