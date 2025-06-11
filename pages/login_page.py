from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    # Locators
    CONTAINER = (By.ID, "account-login")
    LOGIN_BUTTON = (By.XPATH, '//*[@id="form-login"]/div[3]/button')

    def open_page(self, url):
        self.driver.get(url)

    def check_container_exists(self):
        return self.find_element(self.CONTAINER) is not None

    def check_login_button_exists(self):
        return self.find_element(self.LOGIN_BUTTON) is not None
