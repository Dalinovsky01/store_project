import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Filters_page(Base):

    url = 'https://www.livemaster.ru/itemlist/mebel'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators | Локаторы элементов

    # Фильтр сортировки

    sort_dropdown_menu_button = '/html/body/div[1]/div[2]/div[4]/div[2]/div/div[2]/div[2]/div/div/div[2]/button'
    sort_dropdown_menu_button_link = '/html/body/div[1]/div[2]/div[4]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span[4]'

    # Фильтр материала

    material_dropdown_menu_button = '/html/body/div[1]/div[2]/div[4]/div[2]/div/div[2]/div[2]/div/div/div[7]/button'
    glass_material_dropdown_menu_button_link = '//*[@id="material-25"]'
    apply_material_button = '/html/body/div[1]/div[2]/div[4]/div[2]/div/div[2]/div[2]/div/div/div[7]/div/div[2]/div'

    # Фильтр цены

    price_dropdown_menu_button = '/html/body/div[1]/div[2]/div[4]/div[2]/div/div[2]/div[2]/div/div/div[4]/button'
    price_dropdown_menu_min_field = '/html/body/div[1]/div[2]/div[4]/div[2]/div/div[2]/div[2]/div/div/div[4]/div/div[1]/div[1]/div[1]/input'
    price_dropdown_menu_max_field = '/html/body/div[1]/div[2]/div[4]/div[2]/div/div[2]/div[2]/div/div/div[4]/div/div[1]/div[1]/div[2]/input'
    price_apply_button = '/html/body/div[1]/div[2]/div[4]/div[2]/div/div[2]/div[2]/div/div/div[4]/div/div[2]/div'

    # Выбор товара

    product_select_green_chest = '/html/body/div[1]/div[2]/div[4]/div[2]/div/div[3]/div[7]/div/div[1]'


    # Getters | Получение локаторов

    # Фильтр сортировки

    def get_sort_dropdown_menu_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sort_dropdown_menu_button)))

    def get_sort_dropdown_menu_button_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sort_dropdown_menu_button_link)))

    # Фильтр материала

    def get_material_dropdown_menu_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.material_dropdown_menu_button)))

    def get_glass_material_dropdown_menu_button_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.glass_material_dropdown_menu_button_link)))

    def get_apply_material_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.apply_material_button)))

    # Фильтр цены

    def get_price_dropdown_menu_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_dropdown_menu_button)))

    def get_price_dropdown_menu_min_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_dropdown_menu_min_field)))

    def get_price_dropdown_menu_max_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_dropdown_menu_max_field)))

    def get_price_apply_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_apply_button)))

    # Выбор товара

    def get_product_select_green_chest(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_select_green_chest)))


    # Actions | Действия с локаторами

    # Фильтр сортировки

    def click_sort_dropdown_menu_button(self):
        self.get_sort_dropdown_menu_button().click()
        print("Нажатие на выпадающее меню фильтра 'Сортировка'")

    def click_sort_dropdown_menu_button_link(self):
        self.get_sort_dropdown_menu_button_link().click()
        print("Нажатие на ссылку выпадающего меню 'По убыванию цены'")

    # Фильтр материала

    def click_material_dropdown_menu_button(self):
        self.get_material_dropdown_menu_button().click()
        print("Нажатие на выпадающее меню фильтра 'Материал'")

    def click_glass_material_dropdown_menu_button_link(self):
        self.get_glass_material_dropdown_menu_button_link().click()
        print("Выбор материала 'Стекло'")

    def click_apply_material_button(self):
        self.get_apply_material_button().click()
        print("Нажатие на кнопку 'Применить'")

    # Фильтр цены

    def click_price_dropdown_menu_button(self):
        self.get_price_dropdown_menu_button().click()
        print("Нажатие на выпадающее меню фильтра 'Цена'")

    def click_price_dropdown_menu_min_field(self):
        self.get_price_dropdown_menu_min_field().click()
        print("Нажатие на поле ввода минимальной цены")

    def clear_price_dropdown_menu_min_field(self):
        self.get_price_dropdown_menu_min_field().send_keys(Keys.CONTROL + "a")
        self.get_price_dropdown_menu_min_field().send_keys(Keys.BACKSPACE)
        print("Поле максимальной цены отчищено")

    def input_min_price(self, min_price):
        self.get_price_dropdown_menu_min_field().send_keys(min_price)
        print("Ввод минимальной цены")

    def click_price_dropdown_menu_max_field(self):
        self.get_price_dropdown_menu_max_field().click()
        print("Нажатие на поле ввода максимальной цены")

    def clear_price_dropdown_menu_max_field(self):
        self.get_price_dropdown_menu_max_field().send_keys(Keys.CONTROL + "a")
        self.get_price_dropdown_menu_max_field().send_keys(Keys.BACKSPACE)
        print("Поле максимальной цены отчищено")

    def input_max_price(self, max_price):
        self.get_price_dropdown_menu_max_field().send_keys(max_price)
        print("Ввод максимальной цены цены")

    def click_price_apply_button(self):
        self.get_price_apply_button().click()
        print("Нажатие на кнопку 'Применить' в фильтре цены")

    # Выбор товара

    def scroll_to_product_select_green_chest(self):
        self.driver.execute_script("window.scrollTo(0, 800)")

    def click_product_select_green_chest(self):
        self.get_product_select_green_chest().click()
        print("Нажатие на карточку товара")


    # Methods | Универсальные методы для тестов

    def choose_filters(self):

        # Инициализация браузера

        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.assert_url(self.url)
        time.sleep(1)

        # Выбор фильтра сортировки

        self.click_sort_dropdown_menu_button()
        self.click_sort_dropdown_menu_button_link()
        self.get_current_url()
        self.assert_url('https://www.livemaster.ru/itemlist/mebel?sortitems=2')
        time.sleep(1)

        # Выбор фильтра материала

        self.click_material_dropdown_menu_button()
        self.click_glass_material_dropdown_menu_button_link()
        self.click_apply_material_button()
        self.get_current_url()
        self.assert_url('https://www.livemaster.ru/itemlist/mebel?sortitems=2&materials=25')
        time.sleep(1)

        # Выбор фильтра цены

        self.click_price_dropdown_menu_button()

        self.click_price_dropdown_menu_min_field()
        self.clear_price_dropdown_menu_min_field()
        time.sleep(1)
        self.input_min_price(30000)

        self.click_price_dropdown_menu_max_field()
        self.clear_price_dropdown_menu_max_field()
        time.sleep(1)
        self.input_max_price(80000)

        self.click_price_apply_button()
        time.sleep(3)
        self.get_current_url()
        self.assert_url('https://www.livemaster.ru/itemlist/mebel?sortitems=2&materials=25&minprice=30%2C000&maxprice=80%2C000')
        time.sleep(1)

        # Получение скриншота
        self.get_screenshot()

    def select_product(self):
        self.scroll_to_product_select_green_chest()
        time.sleep(1)
        self.click_product_select_green_chest()
        time.sleep(3)
        self.get_current_url()
        self.assert_url('https://www.livemaster.ru/item/41344580-dlya-doma-i-interera-komod-zelenyj-s-otdeleniem-dlya-hraneniy')
        time.sleep(1)

        # Получение скриншота
        self.get_screenshot()