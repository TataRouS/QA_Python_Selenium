# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# # 3.2 Добавить в корзину случайный товар с главной страницы и проверить что он появился в корзине
# from conftest import browser
#
# def test_check_item_in_cart(browser, base_url):
#     browser.get(base_url)
#     wait = WebDriverWait(browser, 5, poll_frequency=1)
#     #browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[3]/div/div[2]/form/div/button[1]').click()
#     time.sleep(1)  # Для демонстрации
#     # Наведение курсора на карусель
#     #actions = ActionChains(browser)
#     element = wait.until(method=EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[2]/div[3]/div/div[2]/form/div/button[1]')),
#                              message="Не появился элемент ('//*[@id=\"content\"]/div[2]/div[3]/div/div[2]/form/div/button[1]/i')")
#     browser.execute_script("arguments[0].scrollIntoView();", element)
#     time.sleep(2)  # Для демонстрации
#     element.click()
#     #     #поиск элемента через ожидание
#     #     right_button = wait.until(method=EC.visibility_of_element_located((By.XPATH, "//*[@id=\"carousel-banner-1\"]/button[2]")),
#     #                message = "Не появился элемент ('//*[@id=\"carousel-banner-1\"]/button[2]')")
#     element2 = wait.until(method=EC.presence_of_element_located(
#         (By.XPATH, '//*[@id="header-cart"]/div/button')),
#                          message="Не появился элемент ('//*[@id=\"header-cart\"]/div/button')")
#     browser.execute_script("arguments[0].scrollIntoView();", element2)
#     time.sleep(2)  # Для демонстрации
#     browser.find_element(By.XPATH, '//*[@id="header-cart"]/div/button').click()
#     time.sleep(2)  # Для демонстрации
#     item_in_cart = wait.until(method = EC.visibility_of_element_located((By.XPATH, "//*[@id=\"header-cart\"]/div/ul/li/table/tbody/tr/td[2]/a")),
#                message="Не появился элемент ('/*[@id=\"header-cart\"]/div/ul/li/table/tbody/tr/td[2]/a')")
#     assert item_in_cart.text == "MacBook", "Текст элемента не соответствует ожидаемому"
#
