from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import browser
import time
# 1 Поиск поля ввода имени
def test_check_my_account_menu(browser, register_account_page_url):
     browser.get(register_account_page_url)
     time.sleep(1) #для демонстрации
     browser.find_element(By.XPATH, "//*[@id=\"top\"]/div/div[2]/ul/li[2]/div/a").click()
     wait = WebDriverWait(browser, 5, poll_frequency=1)
     time.sleep(1)  #для демонстрации
     my_account_menu = wait.until(method = EC.visibility_of_element_located((By.XPATH, '//*[@id="top"]/div/div[2]/ul/li[2]/div/ul/li[2]/a')),
                         message = "Не появился элемент (//*[@id=\"top\"]/div/div[2]/ul/li[2]/div/ul/li[2]/a)")
     assert my_account_menu is not None, "Элемент не найден"
#
#  # 2 Поиск кнопки Continue
# def test_check_button_carousel(browser, register_account_page_url):
#     browser.get(register_account_page_url)
#     wait = WebDriverWait(browser, 10, poll_frequency=1)
#     carousel_item = wait.until(method=EC.visibility_of_element_located((By.XPATH, '//*[@id=\"form-register\"]/div/button')),
#                             message = "Не появился элемент (//*[@id=\"form-register\"]/div/button)")
#     assert carousel_item is not None, "Элемент не найден"
#
#  # 3 Поиск чек-бокс подписки
# def test_check_subscribe_checkbox (browser, register_account_page_url):
#     browser.get(register_account_page_url)
#     wait = WebDriverWait(browser, 3, poll_frequency=1)
#     subscribe_checkbox = wait.until(method=EC.visibility_of_element_located((By.ID, "input-newsletter")),
#                             message = 'Не появился элемент (input-newsletter)')
#     assert subscribe_checkbox is not None, "Элемент не найден"
#
# # 4 Ввод почты
# def test_check_email(browser, register_accaunt_page_url):
#     browser.get(register_accaunt_page_url)
#     wait = WebDriverWait(browser, 2, poll_frequency=1)
#     email = wait.until(method=EC.visibility_of_element_located((By.NAME, 'email')),
#                      message = "Не появился элемент ('email')")
#     assert email is not None, "Элемент не найден"
#
#  # 5 Поиск по тегу h1
# def test_check_header (browser, register_account_page_url):
#     browser.get(register_account_page_url)
#     wait = WebDriverWait(browser, 2, poll_frequency=1)
#     header = wait.until(method=EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/h1')),
#                       message = "Не появился элемент ('//*[@id=\"content\"]/h1')")
#     assert header.text == "Register Account" , "Текст элемента не соответствует ожидаемому"
#
