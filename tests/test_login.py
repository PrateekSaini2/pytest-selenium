import os
import pytest
from selenium.webdriver.common.by import By
from tests.test_base import TestBase

class TestLogin(TestBase):
    locked_user = os.environ.get("SAUCE_LOCKED_USER_NAME", "locked_out_user")
    password = os.environ.get("SAUCE_VALID_PASSWORD")
    
    @pytest.mark.parametrize('username, password', [
        ('standard_user', password), 
        ('locked_out_user', password), 
        ('problem_user', password), 
        ('performance_glitch_user', password)]
        )
    def test_login(self, username, password):
        print(os.getenv("SAUCE_PERFORMANCE_USER_NAME"))
        print(os.environ.get("SAUCE_PERFORMANCE_USER_NAME"))
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()