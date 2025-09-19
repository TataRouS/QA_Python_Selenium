# Удаление товара из списка в разделе администратора
from pages.admin_page import AdminPage
import allure
import uuid

@allure.title(f"Удаление товара из каталога")
@allure.description(f"Проверяет возможность удаления товара из каталога в административной панели")
@allure.feature("Товары / Удаление")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_product_admin_page(browser, base_url):
    admin_page = AdminPage(browser)

    with allure.step("Шаг 1: Открытие страницы логина"):
        admin_page.open_login_page(base_url + "/administration")

    with allure.step("Шаг 2: Вход в систему"):
        admin_page.login("user", "bitnami")

    with allure.step("Шаг 3: Добавление нового товара для последующего удаления"):
        myuuid = uuid.uuid4()
        admin_page.add_new_product("iPhone17", "iphone17", "17Model", str(myuuid))

    with allure.step("Шаг 4: Поиск добавленного товара через фильтр"):
        admin_page.get_new_product_text_from_filter_list("iPhone17")

    with allure.step("Шаг 5: Удаление товара"):
        admin_page.delete_product()

    with allure.step("Шаг 6: Проверка, что список товаров пуст"):
        deleted_product_name = admin_page.get_filter_list().text
        assert deleted_product_name == "No results!", (
            f"Ожидаемое сообщение: 'No results!', получено: '{deleted_product_name}'"
        )
