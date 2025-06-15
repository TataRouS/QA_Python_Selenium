from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент {locator} не найден",
        )

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Элемент {locator} не найден",
        )

    def find_element_presence(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Элемент {locator} не найден",
        )

    def move_to_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        # from selenium.webdriver.common.action_chains import ActionChains
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def click_on_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()

    def scroll_to_element(self, locator, timeout=10):
        element = self.find_element_presence(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)

    def get_text(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        return element.text

    def get_attribute(self, locator, attribute_name, timeout=10):
        element = self.find_element(locator, timeout)
        return element.get_attribute(attribute_name)

    def input_text(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.send_keys(text)

    def get_current_url(self):
        return self.driver.current_url

    def get_element_text(self, locator, timeout=10):
        return self.find_element(locator, timeout).text

    def alert(self, timeout=5):
        try:
            alert = WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            return alert
        except TimeoutException:
            raise Exception("Alert не появился в течение заданного времени")
