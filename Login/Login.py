import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utility.Baseclass import Basepage


class Login(Basepage):
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    submit = (By.CSS_SELECTOR, '.oxd-button')
    click = (By.CSS_SELECTOR, '.oxd-userdropdown-name')
    Logout = (By.LINK_TEXT, "Logout")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):

        # Enter Username and Password
        self.hrm_send_keys(self.username, username)
        self.hrm_send_keys(self.password, password)
        self.hrm_btn_click(self.submit)
        time.sleep(3)

        try:
            # Check if login is successful by looking for user dropdown
            self.hrm_btn_click(self.click)
            self.hrm_btn_click(self.Logout)
            print(f"Login successful for user: {username}")
        except Exception as e:
            print(f"Login failed for user: {username} with error: {str(e)}")

        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
