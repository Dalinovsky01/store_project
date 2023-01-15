import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver

    '''Method get current url'''

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Корректная ссылка " + get_url)

    '''Method assert url | Проверка ссылки'''

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Ссылка совпадает")

    '''Method assert word | Проверка слова'''

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Слово совпадает")

    '''Method screenshot | Скриншот экрана'''

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screen_' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\Dean\\Desktop\\qa_python\\python_selenium\\store_project\\screen\\' + name_screenshot)