import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Product_page(Base):

    url = 'https://www.livemaster.ru/item/41344580-dlya-doma-i-interera-komod-zelenyj-s-otdeleniem-dlya-hraneniy'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators | Локаторы элементов

    add_to_cart_button = '/html/body/div[2]/div[2]/div[2]/div[3]/div[2]/div[3]/button[1]'
    cart_button = '/html/body/div[2]/div[2]/div[2]/div[3]/div[2]/div[3]/a'


    # Getters | Получение локаторов

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))


    # Actions | Действия с локаторами

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print("Нажатие на кнопку 'Добавить в корзину'")

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Нажатие на кнопку 'Перейти в корзину'")


    # Methods | Универсальные методы для тестов

    def add_product_to_cart(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.assert_url(self.url)
        time.sleep(3)

        self.click_add_to_cart_button()
        self.click_cart_button()
        time.sleep(3)
        self.get_current_url()
        self.assert_url('https://www.livemaster.ru/cart')

        # Получение скриншота
        self.get_screenshot()