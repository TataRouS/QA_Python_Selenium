from selenium.webdriver.common.by import By
import time
from conftest import base_url

# 3.1 Написать автотест логина-разлогина в админку с проверкой, что логин был выполнен


def test_login_page(browser, base_url):
    browser.get(base_url + "/administration")
    # Ввод тестовых данных
    browser.find_element(By.ID, "input-username").send_keys("user")
    browser.find_element(By.NAME, "password").send_keys("bitnami")
    # Действия по кнопке
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    # Проверка логирования
    browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/h1')
    time.sleep(2)  # Для демонстрации
