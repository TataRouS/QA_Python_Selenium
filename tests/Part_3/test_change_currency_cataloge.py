import time
from selenium.webdriver.common.by import By
from Currency import change_currency
from conftest import browser

# 3.4 Проверить, что при переключении валют цены на товары меняются в каталоге


def test_check_change_currency_in_cataloge(browser, catalog_page_url, base_url):
    browser.get(catalog_page_url)
    current_currency = browser.find_element(
        By.XPATH, '//*[@id="product-list"]/div/div/div[2]/div/div/span[1]'
    )
    # Cохранение значения переменной при текущем курсе
    currency_value = current_currency.text
    # Функция изменения курса валюты
    change_currency(browser, base_url)
    time.sleep(3)
    browser.get(catalog_page_url)
    time.sleep(3)
    changed_currency = browser.find_element(
        By.XPATH, '//*[@id="product-list"]/div/div/div[2]/div/div/span[1]'
    )
    # Cохранение значения переменной при измененном  курсе
    changed_value = changed_currency.text
    assert changed_value != currency_value, "Цена на товар iMac не изменилась"
