# Добавление нового товара в разделе администратора

from pages.admin_page import AdminPage
import allure
import uuid

@allure.title("Добавление нового товара в админке")
@allure.description("Проверяет возможность добавления нового товара через административную панель")
@allure.feature("Товары / Добавление")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_new_product_admin_page(browser, base_url):
    admin_page = AdminPage(browser)

    with allure.step("Шаг 1: Открытие страницы логина"):
        admin_page.open_login_page(base_url + "/administration")

    with allure.step("Шаг 2: Вход в систему"):
        admin_page.login("user", "bitnami")

    with allure.step("Шаг 3: Добавление нового товара iPhone16"):
        myuuid = uuid.uuid4()
        admin_page.add_new_product("iPhone16", "iphone16", "16Model", str(myuuid))

    with allure.step("Шаг 4: Проверка наличия товара через фильтр"):
        new_product_text = admin_page.get_new_product_text_from_filter_list("iPhone16")[0].text
        print(f"Ожидаемый заголовок: 'iPhone16', получено: '{new_product_text}'")
        assert "iPhone16" in new_product_text, f"Не найден товар 'iPhone16' в списке"
