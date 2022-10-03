from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ex_cond
from selenium.webdriver.support.ui import WebDriverWait
import tests.locator as locator

class TestConstructorTab:
     def test_constructor_tab_transit_to_toppings(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 15)
        wait.until(ex_cond.element_to_be_clickable((By.XPATH, locator.tab_toppings))).click()
        assert wait.until(ex_cond.visibility_of_element_located((By.XPATH, locator.menu_toppings)))

     def test_constructor_tab_transit_to_sauces(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 15)
        wait.until(ex_cond.element_to_be_clickable((By.XPATH, locator.tab_sauces))).click()
        assert wait.until(ex_cond.visibility_of_element_located((By.XPATH, locator.menu_sauces)))

     def test_constructor_tab_transit_to_buns(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 15)
        wait.until(ex_cond.element_to_be_clickable((By.XPATH, locator.tab_toppings))).click()
        wait.until(ex_cond.element_to_be_clickable((By.XPATH, locator.tab_buns))).click()
        assert wait.until(ex_cond.visibility_of_element_located((By.XPATH, locator.menu_buns)))
