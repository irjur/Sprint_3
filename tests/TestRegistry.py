from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ex_cond
from selenium.webdriver.support.ui import WebDriverWait
import tests.locator as locator


class TestRegistry:
    def test_registry_user_valid_password(self, setup):
       self.driver = setup
       wait = WebDriverWait(self.driver, 15)
       self.driver.find_element(By.XPATH, locator.button_personal_account).click()
       self.driver.find_element(By.XPATH, locator.link_registry).click()
       self.driver.find_element(By.XPATH, locator.input_name_on_page_registry).send_keys('Irina')
       self.driver.find_element(By.XPATH, locator.input_email_on_page_registry).send_keys('ir_levina_02_041@yandex.ru')
       self.driver.find_element(By.XPATH, locator.input_password_on_page_registry).send_keys('12345')
       self.driver.find_element(By.XPATH, locator.button_registry).click()
       self.driver.find_element(By.XPATH, locator.button_personal_account).click()
       self.driver.find_element(By.XPATH, locator.input_email_on_page_sign_in).send_keys('ir_levina_02_041@yandex.ru')
       self.driver.find_element(By.XPATH, locator.input_password_on_page_sign_in).send_keys('123456')
       self.driver.find_element(By.XPATH, locator.button_sign_in).click()
       self.driver.find_element(By.XPATH, locator.button_personal_account).click()
       assert wait.until(ex_cond.visibility_of_element_located((By.XPATH, locator.page_account)))

    def test_not_registry_user_not_valid_password(self, setup, registry):
       self.driver = setup
       email = registry
       self.driver.find_element(By.XPATH, locator.button_personal_account).click()
       self.driver.find_element(By.XPATH, locator.link_registry).click()
       self.driver.find_element(By.XPATH, locator.input_name_on_page_registry).send_keys('Irina')
       self.driver.find_element(By.XPATH, locator.input_email_on_page_registry).send_keys(email)
       self.driver.find_element(By.XPATH, locator.input_password_on_page_registry).send_keys('12345')
       self.driver.find_element(By.XPATH, locator.button_registry).click()
       assert self.driver.find_element(By.XPATH, locator.message_error_password)





