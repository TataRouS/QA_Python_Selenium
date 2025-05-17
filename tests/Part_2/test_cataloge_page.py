import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# 1 Поиск меню
def test_check_categories(browser, catalog_page_url):
    browser.get(catalog_page_url)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    categories = wait.until(
        method=EC.visibility_of_element_located((By.ID, "menu")),
        message="Не появился элемент (menu)",
    )
    assert categories is not None, "Элемент не найден"


# 2 Поиск добавления в карзину первого продукта каталога
def test_check_shop_cart_of_first_product(browser, catalog_page_url):
    browser.get(catalog_page_url)
    # Поиск элемента через ожидание
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    shop_cart = wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="product-list"]/div[1]/div/div[2]/form/div/button[1]/i')
        ),
        message='Не появился элемент (//*[@id="product-list"]/div[1]/div/div[2]/form/div/button[1]/i)',
    )
    assert shop_cart is not None, "Элемент не найден"


# 3 Поиск пункта меню в навигатор-бар
def test_check_menu_item(browser, catalog_page_url):
    browser.get(catalog_page_url)
    # Наведение курсора на навигатор-бар
    actions = ActionChains(browser)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    element = wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="narbar-menu"]/ul/li[2]/a')
        ),
        message="Не появился элемент ('//*[@id=\"narbar-menu\"]/ul/li[2]/a')",
    )
    actions.move_to_element(element).perform()
    # Ожидание элемента меню
    wait = WebDriverWait(browser, 5, poll_frequency=1)
    nemu_item = wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="narbar-menu"]/ul/li[2]/div/a')
        ),
        message="Не появился элемент ('/*[@id=\"narbar-menu\"]/ul/li[2]/div/a')",
    )
    assert nemu_item.text == "Show All Laptops & Notebooks", (
        "Текст элемента не соответствует ожидаемому"
    )


# 4 Поиск названия продукта в каталоге
def test_check_category_name(browser, catalog_page_url):
    browser.get(catalog_page_url)
    # Поиск элемента через ожидание
    wait = WebDriverWait(browser, 5, poll_frequency=1)
    product_name = wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="column-left"]/div[1]/a[8]')
        ),
        message="Не появился элемент ('//*[@id=\"column-left\"]/div[1]/a[8]')",
    )
    assert product_name.text == "Phones & PDAs (3)", (
        "Текст элемента не соответствует ожидаемому"
    )


# 5 Поиск категории в меню клик по кнопке в мобильной версии
def test_check_category_on_cklick_menu(browser, catalog_page_url):
    browser.get(catalog_page_url)
    browser.set_window_size(800, 800)
    time.sleep(3)
    browser.find_element(By.XPATH, '//*[@id="menu"]/button').click()
    wait = WebDriverWait(browser, 5, poll_frequency=1)
    category = wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="narbar-menu"]/ul/li[1]/a')
        ),
        message='Не появился элемент (//*[@id="narbar-menu"]/ul/li[1]/a)',
    )
    assert category is not None, "Элемент не найден"
