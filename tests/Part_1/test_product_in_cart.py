from pages.main_page import MainPage


def test_check_item_in_cart(browser, base_url):
    main_page = MainPage(browser)

    # Открытие главной страницы
    main_page.open_main_page(base_url)

    # Добавление первого товара в корзину
    main_page.add_first_product_to_cart()

    # Открытие корзины
    main_page.open_cart()

    # Проверка названия товара в корзине
    item_name = main_page.get_item_name_in_cart()
    assert item_name == "MacBook", (
        f"Ожидаемый товар: 'MacBook', получено: '{item_name}'"
    )
