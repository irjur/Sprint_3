from selenium.webdriver.common.by import By
import tests.locator as locator

class TestExitAccount:
    def test_exit_from_account(self, setup, registry):
       self.driver = setup
       email = registry
       self.driver.find_element(By.XPATH, locator.button_sign_in_account).click()
       self.driver.find_element(By.XPATH, locator.input_email_on_page_sign_in).send_keys(email)
       self.driver.find_element(By.XPATH, locator.input_password_on_page_sign_in).send_keys('123456')
       self.driver.find_element(By.XPATH, locator.button_sign_in).click() #Откровенный костыль, но иначе не работало. Пыталась использовать явное ожидание, но не помогло.
       self.driver.find_element(By.XPATH, locator.button_sign_in).click()
       self.driver.find_element(By.XPATH, locator.button_personal_account).click()
       self.driver.find_element(By.XPATH, locator.button_exit).click()
       self.driver.find_element(By.XPATH, locator.button_personal_account).click()
       assert self.driver.find_element(By.XPATH, locator.page_sign_in)