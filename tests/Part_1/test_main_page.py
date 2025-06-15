from pages.main_page import MainPage


def test_check_carousel_item(browser, base_url):
    main_page = MainPage(browser)
    main_page.open_main_page(base_url)
    assert main_page.check_top_carousel_exists(), "Элемент carousel-banner-0 не найден"


def test_image_from_carousel(browser, base_url):
    main_page = MainPage(browser)
    main_page.open_main_page(base_url)
    assert main_page.check_top_image_exists(), "Картинка из верхней карусели не найдена"


def test_image_starbacks_coffie(browser, base_url):
    main_page = MainPage(browser)
    main_page.open_main_page(base_url)
    assert main_page.check_bottom_image_exists(), (
        "Картинка из нижней карусели не найден"
    )


def test_image_from_carousel_on_click(browser, base_url):
    main_page = MainPage(browser)
    main_page.open_main_page(base_url)
    main_page.hover_on_carousel_navigation()
    assert main_page.click_left_button_and_check_disney_image(), (
        "Изображение Disney не отображается"
    )


def test_right_button_from_carousel(browser, base_url):
    main_page = MainPage(browser)
    main_page.open_main_page(base_url)
    main_page.hover_on_carousel_navigation()
    assert main_page.check_right_button_exists(), "Правая кнопка со стрелкой не найдена"
