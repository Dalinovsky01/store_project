import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Login_page(Base):

    url = "https://www.livemaster.ru/auth/login"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators | Локаторы элементов

    email = '//*[@id="auth-login-page"]'
    cookie_button = '/html/body/div[3]/div[2]/div/button'
    password = '//*[@id="auth-password-page"]'
    login_button = '/html/body/div[1]/div[2]/div[2]/div[1]/div/form/div[4]/div/button'


    # Getters | Получение локаторов

    def get_cookie_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cookie_button)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))


    # Actions | Действия с локаторами

    def click_cookie_button(self):
        self.get_cookie_button().click()
        print("Нажатие кнопки 'Продолжить' в форме использованием куки")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Ввод логина")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Ввод пароля")

    def click_login_button(self):
        self.get_login_button().click()
        print("Нажатие кнопки 'Войти'")


    # Methods | Универсальные методы для тестов

    def authorization(self):

        # Инициализация браузера
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.assert_url(self.url)

        # Авторизация
        self.click_cookie_button()
        time.sleep(1)
        self.input_email('dalinovsky01@gmail.com')
        time.sleep(1)
        self.input_password('QA_test_test1')
        time.sleep(1)
        self.click_login_button()
        time.sleep(5)

        # Проверка перехода на главную страницу
        self.get_current_url()
        self.assert_url('https://www.livemaster.ru/?login=1')

        # Получение скриншота
        self.get_screenshot()
