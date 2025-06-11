from pages.product_page import ProductPage


def test_check_rating(browser, product_page_url):
    product_page = ProductPage(browser)
    product_page.open_page(product_page_url)
    assert product_page.check_product_info_exists(), "Элемент product-info не найден"


def test_check_product_image(browser, product_page_url):
    product_page = ProductPage(browser)
    product_page.open_page(product_page_url)
    assert product_page.check_product_image_exists(), "Изображение товара не найдено"


def test_check_reviews(browser, product_page_url):
    product_page = ProductPage(browser)
    product_page.open_page(product_page_url)
    assert product_page.check_reviews_section(), "Раздел отзывов не отобразился"


def test_check_image_attribute(browser, product_page_url):
    product_page = ProductPage(browser)
    product_page.open_page(product_page_url)
    alt_text = product_page.get_image_alt_attribute()
    assert alt_text == "iMac", (
        f"Атрибут alt изображения должен быть 'iMac', но получено '{alt_text}'"
    )


def test_check_header(browser, product_page_url):
    product_page = ProductPage(browser)
    product_page.open_page(product_page_url)
    header_text = product_page.get_header_h1_text()
    assert header_text == "iMac", (
        f"Заголовок должен быть 'iMac', но получено '{header_text}'"
    )
