import pytest
from selenium.webdriver.common.by import By
from tests.test_base import TestBase

class TestLogin(TestBase):
    @pytest.mark.parametrize('username, password', [
        ('standard_user', 'secret_sauce'), 
        ('locked_out_user', 'secret_sauce'), 
        ('problem_user', 'secret_sauce'), 
        ('performance_glitch_user', 'secret_sauce')]
        )
    def test_login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()