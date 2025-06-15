from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    # Locators
    PRODUCT_INFO_SECTION = (By.ID, "product-info")
    PRODUCT_IMAGE = (By.XPATH, '//*[@id="content"]/div[1]/div[1]/div/div/a[1]/img')
    REVIEWS_LINK = (By.XPATH, '//*[@id="content"]/ul/li[2]/a')
    REVIEW_SECTION = (By.XPATH, '//*[@id="review"]/p')
    IMAGE_ATTRIBUTE = (By.XPATH, '//*[@id="content"]/div[1]/div[1]/div/a/img')
    HEADER_H1 = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/h1')

    def open_page(self, url):
        self.driver.get(url)

    def check_product_info_exists(self):
        return self.find_element(self.PRODUCT_INFO_SECTION) is not None

    def check_product_image_exists(self):
        return self.find_element(self.PRODUCT_IMAGE) is not None

    def check_reviews_section(self):
        self.scroll_to_element(self.REVIEWS_LINK)
        self.click_on_element(self.REVIEWS_LINK)
        return self.find_element(self.REVIEW_SECTION) is not None

    def get_image_alt_attribute(self):
        return self.find_element(self.IMAGE_ATTRIBUTE).get_attribute("alt")

    def get_header_h1_text(self):
        return self.find_element(self.HEADER_H1).text
