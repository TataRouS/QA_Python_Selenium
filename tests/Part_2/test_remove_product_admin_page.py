# Удаление товара из списка в разделе администратора

from pages.admin_page import AdminPage
import uuid


def test_delete_product_admin_page(browser, base_url):
    admin_page = AdminPage(browser)

    # Открытие страницы логина
    admin_page.open_login_page(base_url + "/administration")

    # Ввод данных и вход
    admin_page.login("user", "bitnami")

    # Поиск в каталоге продукта и добавление нового
    myuuid = uuid.uuid4()
    admin_page.add_new_product("iPhone17", "iphone17", "17Model", str(myuuid))

    # Проверка по имени продукту через фильтр
    admin_page.get_new_product_text_from_filter_list("iPhone17")

    admin_page.delete_product()

    deleted_product_name = admin_page.get_filter_list().text

    assert deleted_product_name == "No results!", (
        f"Ожидаемый заголовок: 'iPhone17 удален', получено: '{deleted_product_name}'"
    )
