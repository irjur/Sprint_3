from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ex_cond
from selenium.webdriver.support.ui import WebDriverWait
import tests.locator as locator

class TestSignIn:
    def test_sign_in_by_button_sign_in_account(self, setup, registry):
       self.driver = setup
       email = registry
       self.driver.implicitly_wait(10)
       self.driver.find_element(By.XPATH, locator.button_sign_in_account).click()
       self.driver.find_element(By.XPATH, locator.input_email_on_page_sign_in).send_keys(email)
       self.driver.find_element(By.XPATH, locator.input_password_on_page_sign_in).send_keys('123456')
       self.driver.find_element(By.XPATH, locator.button_sign_in).click()
       self.driver.find_element(By.XPATH, locator.button_sign_in).click()
       assert self.driver.find_element(By.XPATH, locator.page_main)

    def test_sign_in_by_button_personal_account(self, setup, registry):
       self.driver = setup
       email = registry
       self.driver.implicitly_wait(10)
       self.driver.find_element(By.XPATH, locator.button_personal_account).click()
       self.driver.find_element(By.XPATH, locator.input_email_on_page_sign_in).send_keys(email)
       self.driver.find_element(By.XPATH, locator.input_password_on_page_sign_in).send_keys('123456')
       self.driver.find_element(By.XPATH, locator.button_sign_in).click()
       self.driver.find_element(By.XPATH, locator.button_sign_in).click()
       assert self.driver.find_element(By.XPATH, locator.page_main)

    def test_sign_in_by_link_sign_in_page_registry(self, setup, registry):
       self.driver = setup
       email = registry
       self.driver.implicitly_wait(20)
       self.driver.find_element(By.XPATH, locator.button_sign_in_account).click()
       self.driver.find_element(By.XPATH, locator.link_registry).click()
       self.driver.find_element(By.XPATH, locator.link_sign_in).click()
       self.driver.find_element(By.XPATH, locator.input_email_on_page_sign_in).send_keys(email)
       self.driver.find_element(By.XPATH, locator.input_password_on_page_sign_in).send_keys('123456')
       self.driver.find_element(By.XPATH, locator.button_sign_in).click()
       self.driver.find_element(By.XPATH, locator.button_sign_in).click()
       self.driver.find_element(By.XPATH, locator.button_sign_in).click()
       assert self.driver.find_element(By.XPATH, locator.page_main)

    def test_sign_in_by_link_sign_in_page_recover_password(self, setup, registry):
       self.driver = setup
       email = registry
       self.driver.implicitly_wait(10)
       self.driver.find_element(By.XPATH, locator.button_sign_in_account).click()
       self.driver.find_element(By.XPATH, locator.link_recover_password).click()
       self.driver.find_element(By.XPATH, locator.link_sign_in).click()
       self.driver.find_element(By.XPATH, locator.input_email_on_page_sign_in).send_keys(email)
       self.driver.find_element(By.XPATH, locator.input_password_on_page_sign_in).send_keys('123456')
       self.driver.find_element(By.XPATH, locator.button_sign_in).click()
       self.driver.find_element(By.XPATH, locator.button_sign_in).click()
       assert self.driver.find_element(By.XPATH, locator.page_main)
