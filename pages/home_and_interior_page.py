import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Home_and_interior_page(Base):

    url = 'https://www.livemaster.ru/landing/home-interior?utm_source=glavnaya&utm_medium=saydbar&utm_campaign=interer'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators | Локаторы элементов

    furniture_category_link = '/html/body/div[1]/div[2]/div[1]/div[3]/a'


    # Getters | Получение локаторов

    def get_furniture_category_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.furniture_category_link)))


    # Actions | Действия с локаторами

    def click_furniture_category_link(self):
        self.get_furniture_category_link().click()
        print("Нажатие кнопки категории 'Мебель'")


    # Methods | Универсальные методы для тестов

    def choose_category(self):

        # Инициализация браузера
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.assert_url(self.url)
        time.sleep(3)

        # Выбор категории из раздела
        self.click_furniture_category_link()
        time.sleep(3)

        # Проверка ссылки
        self.get_current_url()
        self.assert_url('https://www.livemaster.ru/itemlist/mebel')

        # Получение скриншота
        self.get_screenshot()
