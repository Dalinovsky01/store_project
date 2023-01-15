import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Cart_page(Base):

    url = 'https://www.livemaster.ru/cart'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators | Локаторы элементов

    checkout_button = '//*[@id="accept-purchase-434121"]'


    # Getters | Получение локаторов

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))


    # Actions | Действия с локаторами

    def click_checkout_button(self):

        self.get_checkout_button().click()
        print("Нажатие кнопки 'Перейти к оформлению'")


    # Methods | Универсальные методы для тестов

    def apply_order(self):
        self.get_current_url()
        self.assert_url(self.url)
        self.click_checkout_button()

        # Получение скриншота
        self.get_screenshot()

