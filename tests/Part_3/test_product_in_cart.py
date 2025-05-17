import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 3.2 Добавить в корзину случайный товар с главной страницы и проверить что он появился в корзине


def test_check_item_in_cart(browser, base_url):
    browser.get(base_url)
    wait = WebDriverWait(browser, 5, poll_frequency=1)
    time.sleep(1)  # Для демонстрации
    # Добавление товара в корзину
    element = wait.until(
        method=EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/form/div/button[1]')
        ),
        message="Не появился элемент ('//*[@id=\"content\"]/div[2]/div[1]/div/div[2]/form/div/button[1]')",
    )
    browser.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(2)  # Для демонстрации
    element.click()
    # Переход к кнопке корзины и клик по кнопке
    element2 = wait.until(
        method=EC.presence_of_element_located(
            (By.XPATH, '//*[@id="header-cart"]/div/button')
        ),
        message="Не появился элемент ('//*[@id=\"header-cart\"]/div/button')",
    )
    browser.execute_script("arguments[0].scrollIntoView();", element2)
    time.sleep(7)  # Ожидание исчезноваения уведомления о добавлении товара в корзину
    element2.click()
    time.sleep(2)  # Для демонстрации
    item_in_cart = wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="header-cart"]/div/ul/li/table/tbody/tr/td[2]/a')
        ),
        message="Не появился элемент ('/*[@id=\"header-cart\"]/div/ul/li/table/tbody/tr/td[2]/a')",
    )
    assert item_in_cart.text == "MacBook", "Текст элемента не соответствует ожидаемому"
