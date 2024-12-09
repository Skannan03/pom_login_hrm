# this file will have method for edition, button ,lnk
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Basepage:
    def __init__(self, driver):
        self.driver = driver

    def hrm_send_keys(self, locators, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locators)).send_keys(text)

    def hrm_btn_click(self, locators):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locators)).click()

    def hrm_get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def hrm_click_link(self, locators):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locators)).click()

    def hrm_click_visibility(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
# BASEPAGE
