import time

from selenium import webdriver

from pages.cart_page import Cart_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.home_and_interior_page import Home_and_interior_page
from pages.filters_page import Filters_page
from pages.product_page import Product_page


def test_buy_product():

    # Настройки драйвера
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)

    print("\n\n* * * Start Test * * *")

    # Авторизация

    print("\n\n===== АВТОРИЗАЦИЯ =====")
    login = Login_page(driver)
    login.authorization()

    # Открытие каталога и выбор раздела

    print("\n\n===== ОТКРЫТИЕ КАТАЛОГА И ВЫБОР РАЗДЕЛА =====")
    catalog = Main_page(driver)
    catalog.choose_section()

    # Выбор категории

    print("\n\n===== ВЫБОР КАТЕГОРИИ =====")
    category = Home_and_interior_page(driver)
    category.choose_category()

    # Выбор фильтров

    print("\n\n===== ВЫБОР ФИЛЬТРОВ =====")
    filters = Filters_page(driver)
    filters.choose_filters()

    # Выбор товара

    print("\n\n===== ВЫБОР ТОВАРА =====")
    filters.select_product()
    product = Product_page(driver)
    product.add_product_to_cart()

    # Проверка заказа в корзине
    print("\n\n===== Подтверждение заказа =====")
    cart_check = Cart_page(driver)
    cart_check.apply_order()

    print("\n\n* * * Finish Test * * *")





