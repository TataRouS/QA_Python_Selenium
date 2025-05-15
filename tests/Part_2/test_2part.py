# import time
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# def test_google(browser):
#     browser.get("https://google.com")
#     assert "Google" in browser.title
#
# def test_yandex(browser):
#     browser.get("https://ya.ru")
#     assert "Яндекс" in browser.title
#
# def test_opencart_main(browser, base_url):
#     browser.get(base_url)
#
#     assert "Your Store" in browser.title
#
#
# def test_opencart_admin(browser, base_url):
#     browser.get(base_url + "/administration")
#
#     assert "Administration" in browser.title
#
#
# # 1 Main Page
#
# def test_main_page_menu(browser):
#     time.sleep(1)  # Пауза для демонстрации
#     browser.get(browser.url)
#     carousel_item = browser.find_element(By.ID, "carousel-banner-0")
#     assert not carousel_item is not None, "Элемент не найден"
#
# # 2 Catalog PAge
#
# def test_catalog_page(browser):
#     time.sleep(1)  # Пауза для демонстрации
#     browser.get(browser.url)
#     cataloge_item = browser.find_element(By.PARTIAL_LINK_TEXT, "Mac")
#     assert not cataloge_item is not None, "Элемент не найден"
#
# # 3 Product item
# def test_product_item(browser):
#     time.sleep(1)  # Пауза для демонстрации
#     browser.get(browser.url + "/en-gb/product/desktops/apple-cinema")
#     prоduct_item = browser.find_element(By.TAG_NAME, "h1")
#     assert not prоduct_item is not None, "Элемент не найден"
#
# # 4 Log to Admin
# def test_login_page(browser):
#     browser.get(browser.url + "/administration")
#     browser.find_element(By.ID, "input-username")
#     browser.find_element(By.NAME, "password")
#     browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
#     browser.find_element(By.XPATH, "//*[text()='OpenCart']")
#     time.sleep(2) # Для демонстрации
#
#
# # 5 Accaunt registration
#
# def test_accaunt_registration_page_item(browser):
#     time.sleep(1)  # Пауза для демонстрации
#     browser.get(browser.url + "/en-gb?route=account/register")
#     accaunt_registration_page_item= browser.find_element(By.NAME, "code")
#     assert not accaunt_registration_page_item is not None, "Элемент не найден"
#
#
#
# def test_main_page_fetured_items(browser):
#     time.sleep(1)  # Пауза для демонстрации
#     browser.get(browser.url)
#     fetured_items = browser.find_elements(By.CSS_SELECTOR, ".product-thumb")
#     assert len(fetured_items) == 4, "Неверное количество продуктов в блоке featured"
#
#
# def test_main_page_footer_blocks(browser):
#     time.sleep(1)  # Пауза для демонстрации
#     browser.get(browser.url)
#     footer_blocks = browser.find_elements(By.XPATH, "//footer//ul")
#     time.sleep(1)  # Пауза для демонстрации
#     assert len(footer_blocks) == 4, "Неверное количество списков ссылок в футере"
#
#
# def test_main_page_open_product(browser):
#     browser.get(browser.url)
#     fetured_items = browser.find_elements(By.CLASS_NAME, "product-thumb")
#     fetured_items[2].click()
#     time.sleep(1)  # Пауза для демонстрации
#
#
# 1.1 Написать фикстуру для запуска разных браузеров
# 1.2 Выбор браузера должен осуществляться путем передачи аргумента командной строки pytest
# 1.3 По завершению работы тестов должно осуществляться закрытие браузера
# 1.4 Добавить опцию командной строки, которая указывает базовый URL opencart
#
# Часть 2
# 2.1 Написать тесты проверяющие элементарное наличие элементов на разных страницах приложения opencart
# 2.2 Реализовать минимум пять тестов (одни тест = одна страница приложения)
# 2.3 Использовать методы явного ожидания элементов
#
# Покрыть нужно:
#
# Главную
# Каталог
# Карточку товара
# Страницу логина в админку /administration
# Страницу регистрации пользователя (/index.php?route=account/register)
# Какие именно элементы проверять определить самостоятельно, но не меньше 5 для каждой страницы
#
# Часть 3
# Реализовать покрытие следующих сценариев:
#
# 3.1 Написать автотест логина-разлогина в админку с проверкой, что логин был выполнен
# 3.2 Добавить в корзину случайный товар с главной страницы и проверить что он появился в корзине
# 3.3 Проверить, что при переключении валют цены на товары меняются на главной
# 3.4 Проверить, что при переключении валют цены на товары меняются в каталоге
#
# Критерии оценки:
# Реализованы все проверки перечисленные в задании
# Задание выполнено и сдаётся в формате pull-request
# Соблюдается минимальный код-стайл
# В pull-request отсутствуют лишние файлы не относящиеся к заданию
