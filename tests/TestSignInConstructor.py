from selenium.webdriver.common.by import By
import tests.locator as locator

class TestSignInConctructor:
    def test_sign_in_constructor_from_account_by_button_constructor(self, setup, registry):
       self.driver = setup
       email = registry
       self.driver.implicitly_wait(10)
       self.driver.find_element(By.XPATH, locator.button_sign_in_account).click()
       self.driver.find_element(By.XPATH, locator.input_email_on_page_sign_in).send_keys(email)
       self.driver.find_element(By.XPATH, locator.input_password_on_page_sign_in).send_keys('123456')
       self.driver.find_element(By.XPATH, locator.button_sign_in).click()
       self.driver.find_element(By.XPATH, locator.button_sign_in).click()
       self.driver.find_element(By.XPATH, locator.button_personal_account).click()
       self.driver.find_element(By.XPATH, locator.button_constructor).click()
       assert self.driver.find_element(By.XPATH, locator.page_main)

    def test_sign_in_constructor_from_account_by_logo(self, setup, registry):
       self.driver = setup
       email = registry
       driver.implicitly_wait(20)
       self.driver.find_element(By.XPATH, locator.button_sign_in_account).click()
       self.driver.find_element(By.XPATH, locator.input_email_on_page_sign_in).send_keys(email)
       self.driver.find_element(By.XPATH, locator.input_password_on_page_sign_in).send_keys('123456')
       self.driver.find_element(By.XPATH, locator.button_sign_in).click()
       self.driver.find_element(By.XPATH, locator.button_sign_in).click()
       self.driver.find_element(By.XPATH, locator.button_personal_account).click()
       self.driver.find_element(By.XPATH, locator.logo).click()
       assert self.driver.find_element(By.XPATH, locator.page_main)