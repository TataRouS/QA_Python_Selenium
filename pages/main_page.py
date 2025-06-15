from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class MainPage(BasePage):
    # Locators
    CAROUSEL_TOP = (By.ID, "carousel-banner-0")
    CAROUSEL_TOP_IMAGE = (
        By.XPATH,
        '//*[@id="carousel-banner-0"]/div[2]/div[2]/div/div',
    )
    CAROUSEL_BOTTOM_IMAGE = (
        By.XPATH,
        '//*[@id="carousel-banner-1"]/div[2]/div[2]/div/div[5]/img',
    )
    CAROUSEL_LEFT_BUTTON = (By.XPATH, '//*[@id="carousel-banner-1"]/div[1]/button[1]')
    CAROUSEL_RIGHT_BUTTON = (By.XPATH, '//*[@id="carousel-banner-1"]/button[2]')
    CAROUSEL_NAVIGATION = (By.XPATH, '//*[@id="carousel-banner-1"]/div[1]/button[2]')
    DISNEY_IMAGE = (
        By.XPATH,
        '//*[@id="carousel-banner-1"]/div[2]/div[1]/div/div[3]/img',
    )
    ADD_TO_CART_BUTTON = (
        By.XPATH,
        '//*[@id="content"]/div[2]/div[1]/div/div[2]/form/div/button[1]',
    )
    CART_BUTTON = (By.XPATH, '//*[@id="header-cart"]/div/button')
    ITEM_IN_CART = (By.XPATH, '//*[@id="header-cart"]/div/ul/li/table/tbody/tr/td[2]/a')
    FIRST_PRODUCT_PRICE = (
        By.XPATH,
        '//*[@id="content"]/div[2]/div[1]/div/div[2]/div/div/span[1]',
    )
    CURRENCY_MENU_BUTTON = (By.XPATH, '//*[@id="form-currency"]/div/a')
    CURRENCY_EURO = (By.XPATH, '//*[@id="form-currency"]/div/ul/li[1]/a')

    def open_main_page(self, url):
        self.driver.get(url)

    def check_top_carousel_exists(self):
        return self.find_element(self.CAROUSEL_TOP) is not None

    def check_top_image_exists(self):
        return self.find_element(self.CAROUSEL_TOP_IMAGE) is not None

    def check_bottom_image_exists(self):
        return self.find_element(self.CAROUSEL_BOTTOM_IMAGE) is not None

    def click_left_button_and_check_disney_image(self):
        self.click_on_element(self.CAROUSEL_LEFT_BUTTON)
        disney_image = self.find_element(self.DISNEY_IMAGE)
        return disney_image.get_attribute("alt") == "Disney"

    def hover_on_carousel_navigation(self):
        self.scroll_to_element(self.CAROUSEL_NAVIGATION)
        time.sleep(3)
        self.move_to_element(self.CAROUSEL_NAVIGATION)

    def check_right_button_exists(self):
        return self.find_element(self.CAROUSEL_RIGHT_BUTTON) is not None

    def add_first_product_to_cart(self):
        self.scroll_to_element(self.ADD_TO_CART_BUTTON)
        self.click_on_element(self.ADD_TO_CART_BUTTON)

    def open_cart(self):
        self.scroll_to_element(self.CART_BUTTON)
        time.sleep(3)
        self.click_on_element(self.CART_BUTTON)

    def get_item_name_in_cart(self):
        return self.get_text(self.ITEM_IN_CART)

    def get_product_price(self):
        return self.get_text(self.FIRST_PRODUCT_PRICE)

    def change_currency_to_euro(self):
        self.click_on_element(self.CURRENCY_MENU_BUTTON)
        self.click_on_element(self.CURRENCY_EURO)
