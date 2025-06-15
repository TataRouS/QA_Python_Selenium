# Добавление нового товара в разделе администратора

from pages.admin_page import AdminPage
import uuid


def test_add_new_product_admin_page(browser, base_url):
    admin_page = AdminPage(browser)

    # Открытие страницы логина
    admin_page.open_login_page(base_url + "/administration")

    # Ввод данных и вход
    admin_page.login("user", "bitnami")

    # Поиск в каталоге продукта и добавление нового
    myuuid = uuid.uuid4()
    admin_page.add_new_product("iPhone16", "iphone16", "16Model", str(myuuid))

    # Проверка по имени продукту через фильтр
    new_product_text = admin_page.get_new_product_text_from_filter_list("iPhone16")[
        0
    ].text
    print(f"Ожидаемый заголовок: 'iPhone16', получено: '{new_product_text}'")

    assert "iPhone16" in new_product_text, (
        f"Ожидаемый заголовок: 'iPhone16', получено: '{new_product_text}'"
    )
