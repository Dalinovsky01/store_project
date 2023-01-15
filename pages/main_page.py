import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Main_page(Base):

    url = 'https://www.livemaster.ru/?login=1'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators | Локаторы элементов

    close_modal_button = '/html/body/div[2]/div/div[1]/button'
    catalog_button = '/html/body/div[1]/div[1]/div[2]/div[1]/div/div[1]/button[2]'
    home_and_interior_section_link = '/html/body/div[1]/div[1]/div[2]/div[11]/div/div[1]/div/div/div[2]/div[1]/a'


    # Getters | Получение локаторов

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))

    def get_home_and_interior_section_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.home_and_interior_section_link)))

    def get_close_modal_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.close_modal_button)))


    # Actions | Действия с локаторами

    def click_catalog_button(self):
        self.get_catalog_button().click()
        print("Нажатие кнопки 'Каталог'")

    def click_home_and_interior_section_link(self):
        self.get_home_and_interior_section_link().click()
        print("Нажатие ссылки категории 'Дом и интерьер'")

    def click_close_modal_button(self):
        self.get_close_modal_button().click()
        print("Закрытие модального окна")


    # Methods | Универсальные методы для тестов

    def choose_section(self):

        # Инициализация браузера
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.assert_url(self.url)
        time.sleep(1)

        #Закрытие модального окна, убрать комменатрий, если появляется
        # self.click_close_modal_button()

        # Открытие каталога и выбор раздела
        self.click_catalog_button()
        self.click_home_and_interior_section_link()
        time.sleep(1)

        # Проверка ссылки
        self.get_current_url()
        self.assert_url('https://www.livemaster.ru/landing/home-interior?utm_source=glavnaya&utm_medium=saydbar&utm_campaign=interer')

        # Получение скриншота
        self.get_screenshot()
