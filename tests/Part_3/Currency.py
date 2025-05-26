import time
from selenium.webdriver.common.by import By
from conftest import browser


# Функция изменения валюты
def change_currency(browser, base_url):
    browser.get(base_url)
    browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/a/i').click()
    time.sleep(3)  # Для демонстрации
    currency = browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/a/strong')
    drop_menu = browser.find_elements(By.XPATH, '//*[@id="form-currency"]/div/ul/li')
    time.sleep(3)
    for currelement in drop_menu:
        if currency.text != currelement.text[:1]:  # Первый символ в строке [:1]
            currelement.click()  # Если нашли новую валюту, кликаем на элемент
            break
