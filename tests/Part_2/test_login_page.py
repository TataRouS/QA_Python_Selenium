import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# 1 Поиск по ID
def test_check_container(browser, login_page_url):
    browser.get(login_page_url)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    container = wait.until(
        method=EC.visibility_of_element_located((By.ID, "account-login")),
        message="Не появился элемент (account-login)",
    )
    assert container is not None, "Элемент не найден"


# 2 Поиск кнопки логин
def test_check_login_button(browser, login_page_url):
    browser.get(login_page_url)
    # Поиск элемента через ожидание
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    login_button = wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="form-login"]/div[3]/button')
        ),
        message='Не появился элемент (//*[@id="form-login"]/div[3]/button)',
    )
    assert login_button is not None, "Элемент не найден"


# 3 Поиск пункта меню в top баре Мой аккаунт
def test_check_my_account_item(browser, catalog_page_url):
    browser.get(catalog_page_url)
    # Клик по кнопке меню
    browser.find_element(
        By.XPATH, '//*[@id="top"]/div/div[2]/ul/li[2]/div/a/span'
    ).click()
    # Ожидание элемента меню
    wait = WebDriverWait(browser, 5, poll_frequency=1)
    menu_item = wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="top"]/div/div[2]/ul/li[2]/div/ul/li[2]/a')
        ),
        message="Не появился элемент ('//*[@id=\"top\"]/div/div[2]/ul/li[2]/div/ul/li[2]/a')",
    )
    assert menu_item.text == "Login", "Текст элемента не соответствует ожидаемому"


# 4 Поиск пункта меню в top баре валюта
def test_check_currency(browser, catalog_page_url):
    browser.get(catalog_page_url)
    # Клик по кнопке меню
    browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/a/span').click()
    # Ожидание элемента меню
    wait = WebDriverWait(browser, 5, poll_frequency=1)
    menu_item = wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="form-currency"]/div/ul/li[1]/a')
        ),
        message="Не появился элемент ('//*[@id=\"form-currency\"]/div/ul/li[1]/a')",
    )
    assert menu_item.text == "€ Euro", "Текст элемента не соответствует ожидаемому"


# 5 Поиск категории в меню через клик по кнопке в мобильной версии
def test_check_category_on_cklick_menu(browser, login_page_url):
    browser.get(login_page_url)
    # Оптимизация экрана под мобильную версию
    browser.set_window_size(800, 800)
    time.sleep(3)
    # Клик по кнопке меню
    browser.find_element(By.XPATH, '//*[@id="menu"]/button').click()
    # Поиск элемента через ожидание
    wait = WebDriverWait(browser, 5, poll_frequency=1)
    category = wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="narbar-menu"]/ul/li[1]/a')
        ),
        message='Не появился элемент (//*[@id="narbar-menu"]/ul/li[1]/a)',
    )
    assert category is not None, "Элемент не найден"
