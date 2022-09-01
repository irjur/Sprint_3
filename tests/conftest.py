import pytest #импортируем фреймворк pytest
from selenium import webdriver #импортируем вебдрайвер из селениума
from selenium.webdriver.chrome.options import Options #импортируем опции для вебдрайвера Хром
from selenium.webdriver.common.by import By
import tests.locator as locator


@pytest.fixture
def setup(): #создаем драйвер с нужными опциями и заходим на сайт, который будем тестировать
    chrome_options = Options()  # создали объект для опций
    chrome_options.add_argument('--headless')  # тесты проходят в фоновом режиме. чтоб видеть, как проходят тесты, можно поменять на 'chrome'
    chrome_options.add_argument('--window-size=1920,1080')  # установили разрешение экрана браузера
    driver = webdriver.Chrome(options=chrome_options)  # создали драйвер и передали в него настройки
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def registry(setup): #создаем фикстуру для регистрации на сайте, во многих тестах это предусловие
    email = "ir_levina_02_041@yandex.ru"
    driver = setup
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, locator.button_personal_account).click()
    driver.find_element(By.XPATH, locator.link_registry).click()
    driver.find_element(By.XPATH, locator.input_name_on_page_registry).send_keys('Irina')
    driver.find_element(By.XPATH, locator.input_email_on_page_registry).send_keys(email)
    driver.find_element(By.XPATH, locator.input_password_on_page_registry).send_keys('123456')
    driver.find_element(By.XPATH, locator.button_registry).click()
    driver.find_element(By.XPATH, locator.logo).click()
    return email

