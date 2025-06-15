import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import browser


# 1 Поиск элемента рейтинг
def test_check_rating(browser, product_page_url):
    browser.get(product_page_url)
    wait = WebDriverWait(browser, 5, poll_frequency=1)
    wait.until(
        method=EC.visibility_of_element_located((By.ID, "product-info")),
        message="Не появился элемент (product-info)",
    )
    rating = browser.find_element(By.ID, "product-info")
    assert rating is not None, "Элемент не найден"


# 2 Поиск изображения товара
def test_check_product_image(browser, product_page_url):
    browser.get(product_page_url)
    wait = WebDriverWait(browser, 2, poll_frequency=1)
    product_image = wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="content"]/div[1]/div[1]/div/div/a[1]/img')
        ),
        message='Не появился элемент (//*[@id="content"]/div[1]/div[1]/div/div/a[1]/img)',
    )
    assert product_image is not None, "Элемент не найден"


# 3 Поиск ревью
def test_check_reviews(browser, product_page_url):
    browser.get(product_page_url)
    wait = WebDriverWait(browser, 5, poll_frequency=1)
    # Скролл до элемента
    element = wait.until(
        method=EC.presence_of_element_located(
            (By.XPATH, '//*[@id="content"]/ul/li[2]/a')
        ),
        message="Не появился элемент ('//*[@id=\"content\"]/ul/li[2]/a')",
    )
    browser.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(2)
    element.click()
    reviews = wait.until(
        method=EC.visibility_of_element_located((By.XPATH, '//*[@id="review"]/p')),
        message='Не появился элемент (//*[@id="review"]/p)',
    )
    assert reviews is not None, "Элемент не найден"


# 4 Проверка атрибута изображения
def test_check_image_attribute(browser, product_page_url):
    browser.get(product_page_url)
    wait = WebDriverWait(browser, 5, poll_frequency=1)
    image = wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="content"]/div[1]/div[1]/div/a/img')
        ),
        message="Не появился элемент ('//*[@id=\"content\"]/div[1]/div[1]/div/a/img')",
    )
    assert image.get_attribute("alt") == "iMac", (
        "Текст элемента не соответствует ожидаемому"
    )


# 5 Поиск по тегу h1 iMac
def test_check_header(browser, product_page_url):
    browser.get(product_page_url)
    wait = WebDriverWait(browser, 2, poll_frequency=1)
    header = wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="content"]/div[1]/div[2]/h1')
        ),
        message="Не появился элемент ('//*[@id=\"content\"]/div[1]/div[2]/h1')",
    )
    assert header.text == "iMac", "Текст элемента не соответствует ожидаемому"
