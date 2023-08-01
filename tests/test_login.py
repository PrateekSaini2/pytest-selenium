import os
import pytest
from selenium.webdriver.common.by import By
from tests.test_base import TestBase

class TestLogin(TestBase):
    locked_user = os.environ.get("SAUCE_LOCKED_USER_NAME")
    password = os.environ.get("SAUCE_VALID_PASSWORD")
    performance_glitch_user = os.environ.get("SAUCE_PERFORMANCE_USER_NAME")
    problem_user = os.environ.get("SAUCE_PROBLEM_USER_NAME")
    standard_user = os.environ.get("SAUCE_VALID_USER_NAME")
    
    @pytest.mark.parametrize('username, password', [
        (standard_user, password), 
        (locked_user, password), 
        (problem_user, password), 
        (performance_glitch_user, password)
        ])
    def test_login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()