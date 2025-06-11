from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CatalogPage(BasePage):
    # Locators
    MENU = (By.ID, "menu")
    SHOP_CART_FIRST_PRODUCT = (
        By.XPATH,
        '//*[@id="product-list"]/div[1]/div/div[2]/form/div/button[1]/i',
    )
    NAVBAR_MENU_ITEM = (By.XPATH, '//*[@id="narbar-menu"]/ul/li[2]/a')
    SUBMENU_ITEM = (By.XPATH, '//*[@id="narbar-menu"]/ul/li[2]/div/a')
    CATEGORY_NAME = (By.XPATH, '//*[@id="column-left"]/div[1]/a[8]')
    MOBILE_MENU_BUTTON = (By.XPATH, '//*[@id="menu"]/button')
    MOBILE_CATEGORY_LINK = (By.XPATH, '//*[@id="narbar-menu"]/ul/li[1]/a')
    MY_ACCOUNT_MENU = (By.XPATH, '//*[@id="top"]/div/div[2]/ul/li[2]/div/a/span')
    LOGIN_MENU_ITEM = (By.XPATH, '//*[@id="top"]/div/div[2]/ul/li[2]/div/ul/li[2]/a')
    CURRENCY_MENU = (By.XPATH, '//*[@id="form-currency"]/div/a/span')
    EURO_CURRENCY_ITEM = (By.XPATH, '//*[@id="form-currency"]/div/ul/li[1]/a')
    PRODUCT_PRICE = (By.XPATH, '//*[@id="product-list"]/div/div/div[2]/div/div/span[1]')

    def open_page(self, url):
        self.driver.get(url)

    def check_menu_exists(self):
        return self.find_element(self.MENU) is not None

    def check_first_product_cart_exists(self):
        return self.find_element(self.SHOP_CART_FIRST_PRODUCT) is not None

    def hover_navbar_menu_item(self):
        self.move_to_element(self.NAVBAR_MENU_ITEM)

    def get_submenu_text(self):
        element = self.find_element(self.SUBMENU_ITEM)
        return element.text

    def get_category_name_text(self):
        element = self.find_element(self.CATEGORY_NAME)
        return element.text

    def click_my_account_menu(self):
        self.click_on_element(self.MY_ACCOUNT_MENU)

    def get_login_menu_text(self):
        return self.find_element(self.LOGIN_MENU_ITEM).text

    def click_currency_menu(self):
        self.click_on_element(self.CURRENCY_MENU)

    def get_euro_currency_text(self):
        return self.find_element(self.EURO_CURRENCY_ITEM).text

    def open_mobile_menu(self):
        self.click_on_element(self.MOBILE_MENU_BUTTON)

    def check_mobile_category_exists(self):
        return self.find_element(self.MOBILE_CATEGORY_LINK) is not None

    def get_product_price(self):
        return self.get_text(self.PRODUCT_PRICE)
